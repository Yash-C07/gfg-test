from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import logging
import time

class StackOverflowStatsScraper:
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
        stats = {
            "Reputation": None,
            "Reach": None,
            "Answers": None,
            "Questions": None
            }

        stats_div = soup.find('div', id='stats')
        if stats_div:
            stat_values = stats_div.find_all('div', class_='fs-body3 fc-black-600')
        # The order is usually: Reputation, Reach, Answers, Questions
            labels = ["Reputation", "Reach", "Answers", "Questions"]
            for label, value_div in zip(labels, stat_values):
                stats[label] = value_div.get_text(strip=True).replace(',', '')
        else:
            logging.warning("Could not find stats container.")

        return stats

    def scrape(self):
        try:
            self.load_profile()
            stats = self.parse_stats()
            return stats
        except Exception as e:
            logging.error(f"An error occurred during scraping: {e}")
            if self.driver:
                self.driver.quit()
            return None
