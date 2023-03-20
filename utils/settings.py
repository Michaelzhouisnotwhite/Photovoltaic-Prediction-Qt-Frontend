import os


class __URL__:
    def __str__(self) -> str:
        return "http://127.0.0.1:8089"

    @property
    def verify_data_settings(self):
        return f"{self}/verify-data-settings/"

    @property
    def upload_csv(self):
        return f"{self}/upload-file/"

    @property
    def download_file(self):
        return f"{self}/download-files/"

    def result_file_dir(self, namespace):
        return f"{self}/list-dir/{namespace}"

    @classmethod
    def start_train(cls, namespace):
        return f"{cls}/start-train/{namespace}"


__url__ = __URL__()
SETTINGS_DIR = os.path.abspath(os.path.dirname(__file__))

DEV_DOWNLOAD_DIR = os.path.join(SETTINGS_DIR, "../test")
