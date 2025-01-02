from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def scrape_linkedin(company_name):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in background
    driver = webdriver.Chrome(options=options)
    
    driver.get("https://www.linkedin.com/login")
    
    # LinkedIn credentials (replace with dummy account)
    email = "your_email"
    password = "your_password"
    
    driver.find_element(By.ID, "username").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password, Keys.RETURN)
    
    time.sleep(2)
    search_url = f"https://www.linkedin.com/search/results/people/?keywords={company_name}&origin=SWITCH_SEARCH_VERTICAL"
    driver.get(search_url)
    
    time.sleep(3)
    profiles = driver.find_elements(By.CSS_SELECTOR, '.entity-result__title-text a')
    
    employees = []
    for profile in profiles:
        name = profile.text
        link = profile.get_attribute('href')
        employees.append({"name": name, "profile": link})
    
    driver.quit()
    return employees
