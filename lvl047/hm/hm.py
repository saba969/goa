import re
import requests

def get_social_platform(url):
    
    platforms = {
        'facebook': 'facebook.com',
        'twitter': 'twitter.com',
        'instagram': 'instagram.com',
        'linkedin': 'linkedin.com',
        'github': 'github.com',
    }

    for platform, keyword in platforms.items():
        if keyword in url.lower():
            return platform
    return 'unknown'

def profile_link(url):
    
    platform = get_social_platform(url)
    
    profile_data = {
        'url': url,
        'platform': platform,
        'username': 'unknown',  
        'description': 'No description available' 
    }

    if platform == 'facebook':
        
        profile_data['username'] = 'facebook_user123'
        profile_data['followers'] = 200
        profile_data['description'] = 'Social Media Enthusiast'
    
    elif platform == 'twitter':
       
        profile_data['username'] = 'twitter_user456'
        profile_data['followers'] = 500
        profile_data['description'] = 'Tech Blogger'
    
   

    return profile_data

def extract_links(text):
    
    url_pattern = r'https?://(?:www\.)?(\S+)'
    return re.findall(url_pattern, text)

def social_link_profiler(text):
 
    links = extract_links(text)
    
   
    profiles = []
    for link in links:
        profile = profile_link(link)
        profiles.append(profile)
    
    return profiles

text_input = """
Check out my social profiles: 
Facebook: https://www.facebook.com/facebook_user123
Twitter: https://twitter.com/twitter_user456
Instagram: https://www.instagram.com/instagram_user789
"""

profiles = social_link_profiler(text_input)


for profile in profiles:
    print(f"URL: {profile['url']}")
    print(f"Platform: {profile['platform']}")
    print(f"Username: {profile['username']}")
    print(f"Followers: {profile['followers']}")
    print(f"Description: {profile['description']}\n")

