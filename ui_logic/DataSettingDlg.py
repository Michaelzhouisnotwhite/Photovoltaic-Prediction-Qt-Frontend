import json
import os
from typing import Optional

import PySide6
import requests
from PySide6.QtCore import QSize, Qt, QThread, Signal, Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QDialog, QFileDialog, QLayout,
                               QMainWindow, QMessageBox, QVBoxLayout, QWidget)
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor

from ui.ui_datasettings_dlg import Ui_DataSettingDlg
from ui.ui_upload import Ui_UploadMainWindow
from utils.dev import logger, logger_error
from utils.settings import __url__

from .ui_thread import UploadDataSettingsThread, UploadThread


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
