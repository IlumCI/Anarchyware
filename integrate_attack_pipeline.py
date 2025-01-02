from phishing.bulk_campaign import run_phishing_campaign
from attacks.password_sprayer import password_spray

def integrated_attack_pipeline(company, employees, target_ips, password_list):
    print(f"Starting attack pipeline for {company}")
    
    # Phishing
    run_phishing_campaign(employees, company)
    
    # Password Spraying
    password_spray(target_ips, "admin", password_list)
