import requests
from bs4 import BeautifulSoup
import time

def extract_github_username(profile_url):
    if profile_url.endswith('/'):
        profile_url = profile_url[:-1]
    return profile_url.split('/')[-1]
