from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import logging
import time

class BehanceStatsScraper:
    def __init__(self, profile_url, headless=True, wait_time=5):
        self.profile_url = profile_url
        self.wait_time = wait_time
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def load_profile(self):
        logging.info(f"Loading profile: {self.profile_url}")
        self.driver.get(self.profile_url)
        time.sleep(self.wait_time)

    def parse_stats(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        self.driver.quit()
        stats_labels = ["Project Views", "Appreciations", "Followers", "Following"]
        stats = {label: None for label in stats_labels}
        for row in soup.find_all("tr"):
            tds = row.find_all("td")
            if len(tds) == 2:
                label = tds[0].get_text(strip=True)
                if label in stats:
                    value = tds[1].get_text(strip=True)
                    stats[label] = value
        return stats

    def scrape(self):
        try:
            self.load_profile()
            stats = self.parse_stats()
            return stats
        except (NoSuchElementException, TimeoutException) as e:
            logging.error(f"Error while scraping: {e}")
            self.driver.quit()
            return None
