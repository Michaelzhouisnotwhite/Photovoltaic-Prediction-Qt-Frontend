from PySide6.QtCore import QThread, Signal
import requests


class RequestThread(QThread):
    session = requests.session()
    success_trigger = Signal(dict)
    error_trigger = Signal(dict)

    def __init__(self, url: str) -> None:
        self.url = url
    
    