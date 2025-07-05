import requests
from bs4 import BeautifulSoup

username = "sanyamjanf1x"  # Replace with Sanya's actual GFG username
url = f"https://auth.geeksforgeeks.org/user/{username}/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the coding score on the page
score_element = soup.find("div", text="Coding Score")
if score_element:
    coding_score = score_element.find_next("div").text.strip()
    print(f"{username}'s Coding Score: {coding_score}")
else:
    print("Coding Score not found. The page layout may have changed.")

solved_element = soup.find("div", text="Problem Solved")
if solved_element:
    problem_solved = solved_element.find_next("div").text.strip()
    print(f"{username}'s Problem Solved: {problem_solved}")
else:
    print("Problem Solved not found. The page layout may have changed.")
