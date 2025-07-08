from behance_scraper import BehanceStatsScraper
from utils import setup_logging

def main():
    setup_logging()
    profile_url = input("Enter the Behance profile URL: ").strip()
    if not profile_url.startswith("https://www.behance.net/"):
        print("Invalid Behance profile URL. Please ensure it starts with 'https://www.behance.net/'.")
        return
    scraper = BehanceStatsScraper(profile_url)
    stats = scraper.scrape()
    if stats:
        print("Fetched Behance Stats:")
        for key, value in stats.items():
            print(f"{key}: {value if value else 'Not found'}")
    else:
        print("Failed to fetch stats.")

if __name__ == "__main__":
    main()
