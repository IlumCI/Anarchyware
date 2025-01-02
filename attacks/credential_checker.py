import requests

def check_credentials(api_url, credentials):
    for cred in credentials:
        payload = {"username": cred["username"], "password": cred["password"]}
        response = requests.post(api_url, json=payload)
        
        if response.status_code == 200 and "success" in response.json():
            print(f"Valid credentials found: {cred}")
