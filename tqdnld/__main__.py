import getopt
import os
import sys
import time
from typing import Callable, Optional

from selenium import webdriver

import tqdnld.exceptions as errors

ERROR_CTRL_C = 130
ERROR = 2

HELP_TEXT = "python -m tqdnld --url <URL> [--sleep-after-seconds <Value>] [--scroll-by <Value>]"


def main(argv):
    """
    The main entry point. Invoke with 'python -m tqdnld
    """
    try:
        opts, args = getopt.getopt(argv, None, ["help", "url=", "sleep-after-scroll-seconds=", "scroll-by="])
        url: str = ""
        sleep_after_scroll_seconds: int = 2
        scroll_by: Optional[int] = None

        for opt, arg in opts:
            if opt == "--help":
                print(HELP_TEXT)
                sys.exit()
            elif opt == "--url":
                url = arg
            elif opt == "--sleep-after-scroll-seconds":
                sleep_after_scroll_seconds = int(arg)
            elif opt == "--scroll-by":
                scroll_by = int(arg)

        if url == "":
            print(HELP_TEXT)
            sys.exit(ERROR)

        download(
            url,
            sleep_after_scroll_seconds=sleep_after_scroll_seconds,
            scroll_by=scroll_by)

    except getopt.GetoptError:
        print(HELP_TEXT)
        return sys.exit(ERROR)
    except KeyboardInterrupt:
        return ERROR_CTRL_C


def download(
        url: str,
        on_after_download: Callable[[str], None] = None,
        sleep_after_scroll_seconds: int = 2,
        **kwargs):
    """
    Downloads a URL.
    :param url: The URL to download.
    :param on_after_download: An optional callback to execute after the download completes.
    :param sleep_after_scroll_seconds: The time to sleep after each "scroll" event. Defaults to 2 seconds.
    :param kwargs:
        scroll_by: The number of pixels to scroll by. If omitted the value of 'document.body.scrollHeight' is used.
    """
    driver_path = os.path.join(os.getcwd(), "chromedriver.exe")

    if not os.path.exists(driver_path):
        raise errors.ChromeDriverNotFoundException(driver_path)

    if sleep_after_scroll_seconds < 1:
        raise ValueError("sleep_after_scroll_seconds value must be greater than zero.")

    scroll_by = None

    if kwargs.get("scroll_by") is not None:
        scroll_by = int(kwargs.get("scroll_by"))

        if scroll_by < 1:
            raise ValueError("scroll_by value must be greater than zero.")

    driver = webdriver.Chrome(
        executable_path=os.path.join(os.getcwd(), "chromedriver.exe")
    )

    driver.maximize_window()
    driver.get(url)

    last_height = driver.execute_script("return document.body.scrollHeight")

    if kwargs.get("scroll_by") is not None:
        last_height = driver.execute_script("return window.pageYOffset")

    while True:
        if scroll_by is not None:
            driver.execute_script(f"window.scrollBy(0, {scroll_by})")
        else:
            driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(sleep_after_scroll_seconds)

        if scroll_by is not None:
            new_height = driver.execute_script("return window.pageYOffset")
        else:
            new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height

    if on_after_download is not None:
        on_after_download(driver.page_source)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
