import requests
from bs4 import BeautifulSoup

def scrape_contracts():
    url = "https://www.defense.gov/News/Contracts/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    contracts = []
    for item in soup.find_all('div', class_='contract'):
        company = item.find('strong').text
        description = item.find('p').text
        contracts.append({"company": company, "description": description})
    
    return contracts
