import whois
from datetime import datetime

def get_domain_age(domain):
    try:
        w = whois.whois(domain)
        creation_date = w.creation_date
        
        # Handle multiple creation dates (sometimes it's a list)
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        
        age_days = (datetime.now() - creation_date).days
        return age_days // 365  # Return age in years
    
    except Exception as e:
        return None  # WHOIS lookup failed
