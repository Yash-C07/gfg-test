from stackoverflow_scraper import StackOverflowStatsScraper
from utils import setup_logging

def main():
    setup_logging()
    profile_url = input("Enter the Stack Overflow profile URL: ").strip()
    if not profile_url.startswith("https://stackoverflow.com/users/"):
        print("Invalid Stack Overflow profile URL. Please ensure it starts with 'https://stackoverflow.com/users/'.")
        return
    scraper = StackOverflowStatsScraper(profile_url)
    stats = scraper.scrape()
    print("Stack Overflow Stats:")
    for key, value in stats.items():
        print(f"{key}: {value if value else 'Not found'}")

if __name__ == "__main__":
    main()
