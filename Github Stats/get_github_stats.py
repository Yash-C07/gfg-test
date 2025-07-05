from bs4 import BeautifulSoup
import requests
import time 
from extract_github_username import extract_github_username 

def get_github_stats(profile_url):
    username = extract_github_username(profile_url)
    repos_url = f"https://github.com/{username}?tab=repositories"
    headers = {'User-Agent': 'Mozilla/5.0'}
    repos_page = requests.get(repos_url, headers=headers)
    soup = BeautifulSoup(repos_page.text, "html.parser")

    # Get all repository names
    repo_links = soup.select('a[itemprop="name codeRepository"]')
    repos = [a.text.strip() for a in repo_links]
    total_repos = len(repos)
    total_commits = 0

    for repo in repos:
        commit_count = 0
        found = False
        for branch in ['main', 'master']:
            commits_url = f"https://github.com/{username}/{repo}/commits/{branch}"
            commits_page = requests.get(commits_url, headers=headers)
            if commits_page.status_code == 200:
                commits_soup = BeautifulSoup(commits_page.text, "html.parser")
                # Find the commit count element
                commit_count_elem = commits_soup.find('span', class_='d-none d-sm-inline')
                if commit_count_elem and 'commit' in commit_count_elem.text:
                    # Example text: "256 commits"
                    commit_count_text = commit_count_elem.text.strip().split()[0].replace(',', '')
                    if commit_count_text.isdigit():
                        commit_count = int(commit_count_text)
                        found = True
                        break
        total_commits += commit_count
        time.sleep(0.5)  # Be polite to GitHub's servers
        
    print(f"Username: {username}")
    print(f"Total public repositories: {total_repos}")
    print(f"Total commits (main/master branches): {total_commits}")

