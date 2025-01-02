import requests

HIBP_API_KEY = "your_hibp_api_key"

def check_email_breaches(email):
    headers = {
        'hibp-api-key': HIBP_API_KEY,
        'User-Agent': 'email-breach-checker'
    }
    
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        breaches = response.json()
        return breaches
    return None
