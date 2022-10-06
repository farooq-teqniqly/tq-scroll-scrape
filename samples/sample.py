"""
Scroll and Scrape sample.
"""

import os.path

from tq_scroll_scrape.scroll_and_scrape import ScrollAndScrape


def save_file(source: str):
    filename = os.path.join(os.getcwd(), "sample.html")

    with open(filename, "w") as file:
        file.write(source)


url = "https://www.espn.com/college-football/scoreboard/_/group/80/"
driver_path = os.path.join(os.getcwd(), "../", "chromedriver.exe")
scroll_scraper = ScrollAndScrape(driver_path)
scroll_scraper.download(url, save_file, sleep_after_scroll_seconds=2, scroll_by=1000)
scroll_scraper.driver.close()
scroll_scraper.driver.quit()
