# tqdnld

Python library for downloading web pages via Selenium.

## Usage

### Download ChromeDriver

Download ChromeDriver from https://chromedriver.chromium.org/downloads. Choose the version that matches the Chrome
browser running on your system. Place the executable in the root of your Python project.

### Build tqdnld Wheel

Fork or clone this repository and run `python setup.py bdist_wheel` in the repository root.

### Install tqdnld Wheel

In your consuming project, run `pip install <path to wheel file>`.

### Use the Module

Here is sample code demonstrating how to download a page:

```python
from tqdnld.__main__ import download

url = "https://www.espn.com/"
download(url, sleep_after_scroll_seconds=5, scroll_by=100)
```