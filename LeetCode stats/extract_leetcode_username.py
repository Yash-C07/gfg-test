def extract_leetcode_username(profile_url):
    if profile_url.endswith('/'):
        profile_url = profile_url[:-1]
    return profile_url.split('/')[-1]

