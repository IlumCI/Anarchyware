from github import Github
import re

def scrape_github(company):
    g = Github("your_github_api_token")
    repos = g.search_repositories(query=f"{company} in:name")
    
    sensitive_keywords = ["password", "api_key", "secret", "config"]
    results = []
    
    for repo in repos[:10]:
        contents = repo.get_contents("")
        
        for content in contents:
            if content.type == "file":
                file_data = content.decoded_content.decode('utf-8')
                
                for keyword in sensitive_keywords:
                    if re.search(keyword, file_data, re.IGNORECASE):
                        results.append({"repo": repo.full_name, "file": content.path})
    return results
