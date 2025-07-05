import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from extract_leetcode_username import extract_leetcode_username

def get_leetcode_stats(profile_url):
    username = extract_leetcode_username(profile_url)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(profile_url)
    time.sleep(3)  # Wait for page to load

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    # Find the JSON data in the <script> tag
    script_tag = soup.find('script', id="__NEXT_DATA__")
    if script_tag:
        data = json.loads(script_tag.string)
        # Navigate through the JSON to get stats
        try:
            user_profile = data["props"]["pageProps"]["dehydratedState"]["queries"][0]["state"]["data"]["userProfilePublicProfile"]
            solved_count = user_profile["numAcceptedQuestions"]["all"]
            ranking = user_profile.get("ranking", "N/A")
            acceptance_rate = user_profile.get("acceptanceRate", "N/A")
        except Exception as e:
            solved_count = ranking = acceptance_rate = "N/A"
    else:
        solved_count = ranking = acceptance_rate = "N/A"

    print(f"Username: {username}")
    print(f"Total Problems Solved: {solved_count}")
    print(f"Ranking: {ranking}")
    print(f"Acceptance Rate: {acceptance_rate}")

# Example usage:
profile_link = "https://leetcode.com/fjzzq2002/"
get_leetcode_stats(profile_link)
