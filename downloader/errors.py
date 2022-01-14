class ChromeDriverNotFoundException(Exception):
    """
    Chromedriver.exe was not found in the expected path.
    """

    def __init__(self, expected_path: str):
        """
        Class initializer.
        :param expected_path: The expected path.
        """
        super().__init__(f"Chromedriver.exe was not found at '{expected_path}'")
