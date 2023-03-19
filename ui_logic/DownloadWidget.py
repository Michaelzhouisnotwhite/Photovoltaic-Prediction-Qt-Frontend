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

from ui.ui_result_download_widget import Ui_ResultDownloadWidget
from ui.ui_upload import Ui_UploadMainWindow
from utils.dev import logger, logger_error
from utils.settings import __url__

from .DataSettingDlg import DataSettingDlg
from .ui_thread import UploadDataSettingsThread, UploadThread, GetFileDirThread