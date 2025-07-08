# main.py

from dribbble_scraper import DribbbleStatsScraper
from utils import setup_logging

def main():
    setup_logging()
    profile_url = input("Enter the Dribbble profile URL: ").strip()
    if not profile_url.startswith("https://dribbble.com/"):
        print("Invalid Dribbble profile URL. Please ensure it starts with 'https://dribbble.com/'.")
        return
    scraper = DribbbleStatsScraper(profile_url)
    stats = scraper.scrape()
    print("Dribbble Stats:")
    for key, value in stats.items():
        print(f"{key}: {value if value else 'Not found'}")

if __name__ == "__main__":
    main()
