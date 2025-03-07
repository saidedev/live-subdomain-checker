import requests
import concurrent.futures

def check_subdomain(subdomain):
    try:
        response = requests.get(f"https://{subdomain}", timeout=2)
        if response.status_code < 400:
            print(f"Live: {subdomain} ({response.status_code})")
            return subdomain
    except requests.exceptions.RequestException:
        return None

with open("subdomains.txt") as f:
    subdomains = [line.strip() for line in f]

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    live_subdomains = list(filter(None, executor.map(check_subdomain, subdomains)))

with open("live_subdomains.txt", "w") as f:
    f.write("\n".join(live_subdomains))
