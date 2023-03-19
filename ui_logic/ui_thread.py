import json
from typing import Optional

import os
from utils.settings import __url__
import PySide6
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
from ui.ui_upload import Ui_UploadMainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QLayout, QVBoxLayout, QFileDialog, QMessageBox, QDialog
from PySide6.QtGui import QIcon
from PySide6.QtCore import QThread, Signal, Slot, QSize, Qt

from utils.dev import logger, logger_error
import requests


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


class GetFileDirThread(QThread):
    namespace = ""
    dir_view_trigger = Signal(dict)

    def __init__(self, namespace: str, internal=250, parent=None) -> None:
        super().__init__(parent)
        self.namespace = namespace
        self.internal = internal
        self.stop_flag = False

    def stop(self):
        self.stop_flag = True

    def run(self) -> None:
        try:
            req = requests.get(__url__.result_file_dir(self.namespace))
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

        self.dir_view_trigger.emit(req.json())


class FilesDownloadThread(QThread):
    namespace = ""
    files = []

    def __init__(self, namespace: str, files=None) -> None:
        super().__init__()
        if not files:
            self.files = []
        self.files = files
        self.namespace = namespace

    def run(self) -> None:
        ...


class StartTrainThread(QThread):
    namespace = ""

    def __init__(self, namespace, parent: Optional[PySide6.QtCore.QObject] = None) -> None:
        super().__init__(parent)
        self.namespace = namespace

    def run(self) -> None:
        try:
            req = requests.get(__url__.start_train(self.namespace), headers={"Connection": "Keep-Alive"})
        except RuntimeError as e:
            logger_error(e)
            return
        except requests.exceptions.MissingSchema as e:
            logger_error(e)
            return
        logger(req.json())
        if req.status_code != 200:
            logger_error("start_train_failed")
            logger_error(req.json())
            return
