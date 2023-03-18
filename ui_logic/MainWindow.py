import json
from typing import Optional

import PySide6
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
from ui.ui_upload import Ui_UploadMainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QLayout, QVBoxLayout, QFileDialog, QMessageBox, QDialog
from PySide6.QtGui import QIcon
from PySide6.QtCore import QThread, Signal, Slot
from utils.dev import logger, logger_error
import requests
import os
from utils.settings import __url__
# from ui.ui_datasettings import Ui_DataSettingDlg
from ui.ui_result_download_widget import Ui_ResultDownloadWidget
from ui.ui_main_window import Ui_MainWindow
from ui.ui_datasettings_dlg import Ui_DataSettingDlg
__FILE_DIR__ = os.path.abspath(os.path.dirname(__file__))


class UploadThread(QThread):
    upload_progress = Signal(int)
    file_path: str = ""
    thread_running = True
    namespace = ""

    class FilePathNotExits(RuntimeError):
        message = ""

        def __init__(self, message="") -> None:
            self.message = message

        def __str__(self) -> str:
            return self.message

    def __init__(self) -> None:
        super().__init__()

    def set_namespace(self, namespace: str):
        self.namespace = namespace

    def set_upload_file_path(self, file_path: str):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            raise FileExistsError()

    def exit(self, retcode: int = ...) -> None:
        self.file_path = ""
        return super().exit(retcode)

    def quit(self) -> None:
        self.file_path = ""
        return super().quit()

    def stop_thread(self):
        self.file_path = ""
        self.thread_running = False

    def upload_monitor(self, upload_bytes: MultipartEncoderMonitor):
        logger(f"bytes upload: {upload_bytes.bytes_read / os.path.getsize(self.file_path) * 100}")
        self.upload_progress.emit(upload_bytes.bytes_read / os.path.getsize(self.file_path) * 100)

    def run(self) -> None:
        file_name = os.path.split(self.file_path)[-1]
        data = MultipartEncoder(fields={
            "file": (file_name, open(self.file_path, 'rb')),
            "size": str(os.path.getsize(self.file_path)),
            "namespace": self.namespace
        })
        data = MultipartEncoderMonitor(data, self.upload_monitor)
        headers = {"Content-Type": data.content_type}
        try:
            req = requests.post(__url__.upload_csv, data=data, headers=headers)
        except RuntimeError as e:
            logger_error(e)
            return
        except requests.exceptions.MissingSchema as e:
            logger_error(e)
            return
        logger(req.json())
        if req.status_code != 200:
            logger_error("upload file failed")
            logger_error(req.json())
            return


class UploadDataSettingsThread(QThread):
    train_seq_len: int = 96
    predict_len: int = 10
    upload_result = dict()
    payload = dict()

    def __init__(self, namespace="", train_seq_len=96, predict_len=10):
        super().__init__()
        self.payload = dict(namespace=namespace, train_seq_len=train_seq_len, predict_len=predict_len)

    def run(self) -> None:
        try:
            req = requests.post(__url__.verify_data_settings, json=self.payload)
        except RuntimeError as e:
            logger_error(e)
            return
        except requests.exceptions.MissingSchema as e:
            logger_error(e)
            return
        logger(req.json())
        if req.status_code != 200:
            logger_error("verify data settings failed")
            logger_error(req.json())
            return

        self.upload_result = req.json()


class DataSettingDlg(QDialog):
    def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = None) -> None:
        super().__init__(parent)
        self.data_settings_ui = Ui_DataSettingDlg()
        self.data_settings_ui.setupUi(self)

        self.data_settings_ui.okButton.clicked.connect(self.accept)
        self.data_settings_ui.cancelButton.clicked.connect(self.reject)
        self.namespace = None

    def accept(self) -> None:
        upload_data_settings_thread = UploadDataSettingsThread(
            self.data_settings_ui.nameSpaceEdit.text(),
            int(self.data_settings_ui.seqLenSpinBox.text()),
            int(self.data_settings_ui.predictLenSpinBox.text())
        )
        upload_data_settings_thread.start()
        upload_data_settings_thread.wait()

        if upload_data_settings_thread.upload_result["code"] == 200:
            self.namespace = upload_data_settings_thread.payload["namespace"]
            return super().accept()

        else:
            msgbox = QMessageBox(self)
            msgbox.setText(upload_data_settings_thread.upload_result["message"])
            msgbox.setIcon(QMessageBox.Icon.Warning)
            msgbox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgbox.exec()
            self.data_settings_ui.nameSpaceEdit.focusWidget()
            self.data_settings_ui.nameSpaceEdit.selectAll()

    def reject(self) -> None:
        return super().reject()


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.upload_ui = Ui_UploadMainWindow()
        self.upload_ui.setupUi(self)
        self.setWindowIcon(QIcon(os.path.join(__FILE_DIR__, "../ui/icon/upload-128.png")))
        self.upload_ui.uploadStackedWidget.setCurrentIndex(0)
        self.upload_thread = UploadThread()

        self.data_settings_dlg = DataSettingDlg(self)

    def browse_computer_btn_clicked(self):
        logger("browse_computer_btm_clicked")

        if self.data_settings_dlg.exec():
            ...
        else:
            return
        if self.upload_thread.isRunning():
            self.upload_thread.stop_thread()
            self.upload_thread.wait()
            self.upload_thread.upload_progress.disconnect()

        self.upload_ui.fileUploadProgressBar.setValue(0)
        self.upload_thread = UploadThread()
        fileDlg = QFileDialog(self, u"打开要预测的数据集文件", filter="CSV文件 (*.csv)")
        fileDlg.setWindowIcon(QIcon(os.path.join(__FILE_DIR__, "../ui/icon/csv-red.ico")))
        fileDlg.setFileMode(QFileDialog.FileMode.ExistingFile)
        fileDlg.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)

        if fileDlg.exec():
            file_names = fileDlg.selectedFiles()
            self.upload_thread.set_namespace(self.data_settings_dlg.namespace)
            self.upload_thread.set_upload_file_path(file_names[-1])

            # 上传成功UI更新
            self.upload_thread.upload_progress.connect(self.refresh_progress_bar)
            self.upload_ui.uploadStackedWidget.setCurrentIndex(1)
            self.upload_ui.uploadCompleteLabel.setText("正在上传文件...")
            self.upload_ui.browseComputerBtn.setText("重新上传文件")
            self.upload_ui.browseComputerBtn.clicked.disconnect()
            self.upload_ui.browseComputerBtn.clicked.connect(self.rebrowse_computer_btn_clicked)
            self.upload_ui.fileNameLabel.setText(os.path.split(file_names[0])[-1])

            # 上传线程
            self.upload_thread.start()
            self.upload_thread.finished.connect(self.upload_file_success)
            logger(file_names)

    @Slot()
    def upload_file_success(self):
        msgbox = QMessageBox(
            QMessageBox.Icon.Information,
            "",
            u"是否训练",
            buttons=QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel,
            parent=self)
        ret = msgbox.exec()
        if ret == QMessageBox.StandardButton.Save:
            ...
        else:
            ...
        ...

    def rebrowse_computer_btn_clicked(self):
        msg_box = QMessageBox()
        self.browse_computer_btn_clicked()
        ...

    def __del__(self):
        ...

    @Slot(int, name="refresh progress bar")
    def refresh_progress_bar(self, cur_progress: int):
        self.upload_ui.fileUploadProgressBar.setValue(cur_progress)
