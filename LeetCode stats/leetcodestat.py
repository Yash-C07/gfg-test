import requests

username = input("Paste you're Leetcode username here") 
url = f"https://leetcode-stats-api.herokuapp.com/{username}"
response = requests.get(url)
data = response.json()

print(f"Username: {username}")
print(f"Total Problems Solved: {data['totalSolved']}")
print(f"Ranking: {data['ranking']}")
print(f"Acceptance Rate: {data['acceptanceRate']}")
