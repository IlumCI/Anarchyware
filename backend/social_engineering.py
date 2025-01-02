from linkedin_scraper import scrape_linkedin
from github_scraper import scrape_github
from hibp_checker import check_email_breaches

def social_engineering_pipeline(company):
    print(f"Running social engineering recon for {company}...")
    
    # LinkedIn Scraping
    employees = scrape_linkedin(company)
    print(f"Employees Found: {len(employees)}")
    
    # GitHub Leak Scan
    leaks = scrape_github(company)
    print(f"Leaked Repos Detected: {len(leaks)}")
    
    # Email Breach Check
    breach_results = []
    for employee in employees:
        email = employee['name'].replace(" ", ".").lower() + "@company.com"
        breaches = check_email_breaches(email)
        if breaches:
            breach_results.append({"email": email, "breaches": breaches})
    
    return {"employees": employees, "github_leaks": leaks, "breached_emails": breach_results}
