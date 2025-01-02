from phishing_email import send_phishing_email

def run_phishing_campaign(employee_list, company_name):
    for employee in employee_list:
        email = employee["email"]
        send_phishing_email(email, company_name)
