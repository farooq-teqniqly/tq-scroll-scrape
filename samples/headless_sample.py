"""
Scroll and Scrape headless sample.
"""

import os.path

from tq_scroll_scrape.scroll_and_scrape import ScrollAndScrape


def save_file(source: str):
    """
        Saves the downloaded content to a file.
    """
    filename = os.path.join(os.getcwd(), "headless_sample.html")

    with open(filename, "w", encoding="utf-8") as file:
        file.write(source)


URL = "https://www.espn.com"
driver_path = os.path.join(os.getcwd(), "../", "chromedriver.exe")
scroll_scraper = ScrollAndScrape(driver_path, headless=True)
scroll_scraper.download(URL, save_file, sleep_after_scroll_seconds=2, scroll_by=1000)
scroll_scraper.driver.close()
scroll_scraper.driver.quit()
