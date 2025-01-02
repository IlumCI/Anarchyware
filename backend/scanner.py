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

    except shodan.APIError as e:
        return {"error": str(e)}
