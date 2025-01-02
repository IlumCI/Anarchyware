import socket
import ssl

def check_ssl(hostname):
    ctx = ssl.create_default_context()
    conn = ctx.wrap_socket(socket.socket(), server_hostname=hostname)
    
    try:
        conn.connect((hostname, 443))
        cert = conn.getpeercert()
        ssl_version = conn.version()
        
        expiry_date = ssl.cert_time_to_seconds(cert['notAfter'])
        remaining_days = (expiry_date - ssl.time.time()) // 86400
        
        return {"ssl_version": ssl_version, "valid_days": remaining_days}
    
    except Exception as e:
        return {"error": str(e)}
