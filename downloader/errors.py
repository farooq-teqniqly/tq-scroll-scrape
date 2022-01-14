class ChromeDriverNotFoundException(Exception):
    def __init__(self, expected_path: str):
        super().__init__(f"Chromedriver.exe was not found at '{expected_path}'")
