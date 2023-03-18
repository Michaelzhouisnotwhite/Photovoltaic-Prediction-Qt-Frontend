class __URL__:
    def __str__(self) -> str:
        return "http://127.0.0.1:8089"

    @property
    def verify_data_settings(self):
        return f"{self}/verify-data-settings/"
    @property
    def upload_csv(self):
        return f"{self}/upload-file/"
    upload_csv_progress = ""
    
__url__ = __URL__()
