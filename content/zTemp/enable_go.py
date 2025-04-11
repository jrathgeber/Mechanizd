import subprocess
import os
import sys

def install_certbot():
    subprocess.run(['apt-get', 'update'])
    subprocess.run(['apt-get', 'install', 'certbot', '-y'])

def obtain_ssl_certificate(domain):
    subprocess.run(['certbot', 'certonly', '--standalone', '-d', domain])

def configure_apache(domain):
    ssl_conf = f"""
<VirtualHost *:443>
    ServerName {domain}
    DocumentRoot /var/www/html
    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/{domain}/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/{domain}/privkey.pem
</VirtualHost>
"""
    with open(f'/etc/apache2/sites-available/{domain}-ssl.conf', 'w') as f:
        f.write(ssl_conf)
    
    subprocess.run(['a2ensite', f'{domain}-ssl.conf'])
    subprocess.run(['systemctl', 'reload', 'apache2'])

def main():
    if os.geteuid() != 0:
        print("This script must be run as root.")
        sys.exit(1)

    domain = input("Enter your domain name: ")

    install_certbot()
    obtain_ssl_certificate(domain)
    configure_apache(domain)

    print(f"SSL certificate has been enabled for {domain}")

if __name__ == "__main__":
    main()