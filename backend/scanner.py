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
    except shodan.APIError as e:
        return {"error": str(e)}
