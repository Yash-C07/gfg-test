from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import logging
import time

class DribbbleStatsScraper:
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
        stats = {"Followers": None, "Following": None, "Likes": None}

        masthead_stats_div = soup.find('div', class_='masthead-stats')
        if masthead_stats_div:
            stat_divs = masthead_stats_div.find_all('div', class_='stat')
            for div in stat_divs:
                text = div.get_text(strip=True).lower()
                number = div.get_text(strip=True).split(' ')[0].replace(',', '')
                if 'followers' in text:
                    stats["Followers"] = number
                elif 'following' in text:
                    stats["Following"] = number
                elif 'likes' in text:
                    stats["Likes"] = number
        else:
            logging.warning("Could not find 'masthead-stats' div. Stats might not be present or selector is incorrect.")
            
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
