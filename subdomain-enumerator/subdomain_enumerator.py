import requests
import socket
from concurrent.futures import ThreadPoolExecutor

WORDLIST = [
    'www', 'mail', 'api', 'dev', 'test', 'admin', 'blog'
]

found = []


def check_subdomain(domain, subdomain):
    url = f"http://{subdomain}.{domain}"

    try:
        requests.get(url, timeout=2)
        ip = socket.gethostbyname(f"{subdomain}.{domain}")
        print(f"[FOUND] {url} -> {ip}")
        found.append(url)
    except:
        pass


def main():
    domain = input('Enter target domain: ')

    with ThreadPoolExecutor(max_workers=20) as executor:
        for subdomain in WORDLIST:
            executor.submit(check_subdomain, domain, subdomain)

    print(f"\nTotal Found: {len(found)}")


if __name__ == '__main__':
    main()
