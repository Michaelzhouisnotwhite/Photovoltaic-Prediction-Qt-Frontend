import json
import os
from typing import Optional

import PySide6
import requests
from PySide6.QtCore import QSize, Qt, QThread, Signal, Slot, QModelIndex, QPersistentModelIndex
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QDialog, QFileDialog, QLayout,
                               QMainWindow, QMessageBox, QVBoxLayout, QWidget, QTreeWidget, QTreeWidgetItem, QHeaderView, QAbstractItemView)
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor

from ui.ui_main_window import Ui_MainWindow
from ui.ui_result_download_widget import Ui_ResultDownloadWidget
from ui.ui_upload import Ui_UploadMainWindow
from utils.dev import logger, logger_error
from utils.settings import __url__

from .DataSettingDlg import DataSettingDlg
from .ui_thread import UploadDataSettingsThread, UploadThread, GetFileDirThread, StartTrainThread, FilesDownloadThread
from . import __MODULE_DIR__


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        # self.main_window = Ui_MainWindow()
        # self.main_window.setupUi(self)

        self.upload_widget_size = (574, 276)
        self.download_widget_size = (672, 431)
        self.upload_widget = Ui_UploadMainWindow()
        self.upload_thread = UploadThread()
        self.data_settings_dlg = DataSettingDlg(self)
        self.result_download_widget = Ui_ResultDownloadWidget()
        self.get_file_dir_thread: GetFileDirThread = None

        self.init_upload_widget()

    def init_upload_widget(self):
        temp_widget = QWidget(self)
        self.upload_widget.setupUi(temp_widget)
        self.setCentralWidget(temp_widget)
        self.setWindowTitle(temp_widget.windowTitle())
        self.setMaximumSize(temp_widget.maximumSize())
        self.resize(*self.upload_widget_size)
        self.upload_widget.uploadStackedWidget.setCurrentIndex(0)
        # self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)
        self.upload_widget.browseComputerBtn.clicked.connect(self.browse_computer_btn_clicked)
        self.setWindowIcon(QIcon(os.path.join(__MODULE_DIR__, "../ui/icon/upload-128.png")))

    def init_download_widget(self):
        temp_widget = QWidget(self)
        self.resize(*self.download_widget_size)
        self.result_download_widget.setupUi(temp_widget)
        self.setCentralWidget(temp_widget)
        self.result_download_widget.dirTreeWidget.setColumnCount(3)
        self.result_download_widget.dirTreeWidget.setHeaderLabels([u"文件名 (File Name)", u"大小 (Size)", u"类型 (Type)"])
        self.setWindowTitle(temp_widget.windowTitle())
        self.setMaximumSize(16777215, 16777215)
        # self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)
        self.setMinimumSize(0, 0)
        self.setWindowIcon(QIcon(os.path.join(__MODULE_DIR__, "../ui/icon/download-128.png")))
        self.result_download_widget.refreshBtn.clicked.connect(self.tree_view_refresh)
        self.result_download_widget.dirTreeWidget.setSelectionMode(QTreeWidget.SelectionMode.SingleSelection)
        self.result_download_widget.dirTreeWidget.itemChanged.connect(self.dir_tree_item_changed)

        self.tree_expanded_dict = dict()
        self.result_download_widget.dirTreeWidget.itemExpanded.connect(self.tree_widget_item_expanded)
        self.result_download_widget.dirTreeWidget.itemCollapsed.connect(self.tree_widget_item_collapsed)
        self.result_download_widget.downloadBtn.clicked.connect(self.download_btn_clicked)

    @Slot()
    def download_btn_clicked(self):
        ...

    @Slot(QTreeWidgetItem)
    def tree_widget_item_expanded(self, item: QTreeWidgetItem):
        self.tree_expanded_dict[item.text(0)] = True

    @Slot(QTreeWidgetItem)
    def tree_widget_item_collapsed(self, item: QTreeWidgetItem):
        self.result_download_widget.dirTreeWidget.expand_items_idx[item.text(0)] = False

    @Slot(QTreeWidgetItem, int)
    def dir_tree_item_changed(self, item: QTreeWidgetItem, item_id: int):
        item_child_count = item.childCount()
        if item_child_count:
            if item.checkState(0) == Qt.CheckState.Checked:
                for i in range(item_child_count):
                    item.child(i).setCheckState(0, Qt.CheckState.Checked)

            elif item.checkState(0) == Qt.CheckState.Unchecked:
                for i in range(item_child_count):
                    item.child(i).setCheckState(0, Qt.CheckState.Unchecked)
        else:
            item_parent = item.parent()
            if not item_parent:
                return

            selected_child_count = 0
            for i in range(item_parent.childCount()):
                if item_parent.child(i).checkState(0) == Qt.CheckState.Checked:
                    selected_child_count += 1

            if selected_child_count == 0:
                item_parent.setCheckState(0, Qt.CheckState.Unchecked)

            elif item_parent.childCount() > selected_child_count > 0:
                item_parent.setCheckState(0, Qt.CheckState.PartiallyChecked)

            elif selected_child_count == item_parent.childCount():
                item_parent.setCheckState(0, Qt.CheckState.Checked)

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

        self.upload_widget.fileUploadProgressBar.setValue(0)
        self.upload_thread = UploadThread()
        fileDlg = QFileDialog(self, u"打开要预测的数据集文件", filter="CSV文件 (*.csv)")
        fileDlg.setWindowIcon(QIcon(os.path.join(__MODULE_DIR__, "../ui/icon/csv-red.ico")))
        fileDlg.setFileMode(QFileDialog.FileMode.ExistingFile)
        fileDlg.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)

        if fileDlg.exec():
            file_names = fileDlg.selectedFiles()
            self.upload_thread.set_namespace(self.data_settings_dlg.namespace)
            self.upload_thread.set_upload_file_path(file_names[-1])

            # 上传成功UI更新
            self.upload_thread.upload_progress.connect(self.refresh_progress_bar)
            self.upload_widget.uploadStackedWidget.setCurrentIndex(1)
            self.upload_widget.uploadCompleteLabel.setText("正在上传文件...")
            self.upload_widget.browseComputerBtn.setText("重新上传文件")
            self.upload_widget.browseComputerBtn.clicked.disconnect()
            self.upload_widget.browseComputerBtn.clicked.connect(self.rebrowse_computer_btn_clicked)
            self.upload_widget.fileNameLabel.setText(os.path.split(file_names[0])[-1])

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
        msgbox.button(QMessageBox.StandardButton.Ok).setText(u"是")
        msgbox.button(QMessageBox.StandardButton.Cancel).setText(u"否")
        ret = msgbox.exec()
        if ret == QMessageBox.StandardButton.Ok:
            # TODO: 请求后端开始训练
            self.init_download_widget()
            ...
        else:
            ...
        ...

    @Slot()
    def tree_view_refresh(self):
        if isinstance(self.get_file_dir_thread, GetFileDirThread):
            self.get_file_dir_thread.stop()
            self.get_file_dir_thread.wait()
        self.get_file_dir_thread = GetFileDirThread(self.data_settings_dlg.namespace)
        self.get_file_dir_thread.start()
        self.result_download_widget.dirTreeWidget.setDisabled(True)
        self.result_download_widget.refreshBtn.setDisabled(True)
        self.get_file_dir_thread.dir_view_trigger.connect(self.update_tree_view)

    def update_tree_view(self, data):
        self.result_download_widget.dirTreeWidget.setDisabled(False)
        self.result_download_widget.refreshBtn.setDisabled(False)

        items = []
        if data["code"] != 200:
            ...
        for i, (result_type_name, result_type_values) in enumerate(data["data"].items()):
            item = QTreeWidgetItem([result_type_name])
            item.setCheckState(0, Qt.CheckState.Unchecked)

            for file_name, file_size in result_type_values:
                _, ext = os.path.splitext(file_name)
                if file_size < 2**10:
                    wi = QTreeWidgetItem([file_name, f"{(file_size):.2f}B", ext])
                elif 2**10 <= file_size < 2**20:
                    wi = QTreeWidgetItem([file_name, f"{(file_size / 2**10):.2f}KB", ext])
                elif 2**20 <= file_size < 2**30:
                    wi = QTreeWidgetItem([file_name, f"{(file_size / 2**20):.2f}MB", ext])
                else:
                    wi = QTreeWidgetItem([file_name, f"{(file_size / 2**30):.2f}GB", ext])
                wi.setCheckState(0, Qt.CheckState.Unchecked)
                item.addChild(wi)
            items.append(item)

        self.result_download_widget.dirTreeWidget.clear()
        self.result_download_widget.dirTreeWidget.addTopLevelItems(items)
        self.result_download_widget.dirTreeWidget.header().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.result_download_widget.dirTreeWidget.header().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.result_download_widget.dirTreeWidget.expandAll()
        self.tree_expanded_dict.clear()

    def rebrowse_computer_btn_clicked(self):
        msg_box = QMessageBox()
        self.browse_computer_btn_clicked()
        ...

    def __del__(self):
        ...

    @Slot(int, name="refresh progress bar")
    def refresh_progress_bar(self, cur_progress: int):
        self.upload_widget.fileUploadProgressBar.setValue(cur_progress)
