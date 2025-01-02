import shodan

API_KEY = 'YOUR_SHODAN_API_KEY'
api = shodan.Shodan(API_KEY)

def run_scan(ip):
    try:
        result = api.host(ip)
        vulns = result.get('vulns', [])
        return {
            "ip": ip,
            "vulnerabilities": vulns,
            "ports": [service['port'] for service in result['data']]
        }

    def calculate_score(vulns, ports):
    score = 0
    critical_ports = {22, 3389, 21, 25}
    
    for vuln in vulns:
        cvss = vuln.get('cvss', {}).get('base', 0)
        if cvss > 8:
            score += 40
        elif cvss >= 5:
            score += 20
    
    for port in ports:
        if port in critical_ports:
            score += 25
    
    return min(score, 100)  # Cap score at 100

    def run_scan(ip):
    try:
        result = api.host(ip)
        vulns = result.get('vulns', [])
        ports = [service['port'] for service in result['data']]
        score = calculate_score(vulns, ports)
        
        conn = connect()
        cur = conn.cursor()
        cur.execute("UPDATE targets SET score = %s WHERE ip = %s", (score, ip))
        conn.commit()
        conn.close()
        
        return {"ip": ip, "vulnerabilities": vulns, "score": score}

    from whois_checker import get_domain_age
from ssl_checker import check_ssl

def calculate_score(vulns, ports, domain):
    score = 0
    critical_ports = {22, 3389, 21, 25}
    
    # Base vulnerability and port scan scoring
    for vuln in vulns:
        cvss = vuln.get('cvss', {}).get('base', 0)
        if cvss > 8:
            score += 40
        elif cvss >= 5:
            score += 20
    
    for port in ports:
        if port in critical_ports:
            score += 25

    # WHOIS domain age check
    age = get_domain_age(domain)
    if age and age > 5:
        score += 5  # Older domains get flagged
    
    # SSL Check
    ssl_result = check_ssl(domain)
    if ssl_result.get('valid_days', 0) < 30:
        score += 10  # Expiring SSL certs get flagged
    
    return min(score, 100)  # Cap at 100

    
    except shodan.APIError as e:
        return {"error": str(e)}
