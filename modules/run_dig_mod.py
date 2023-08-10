import subprocess
import re

def run_dig(domain):
    try:
        result = subprocess.run(["dig", "+short", domain], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout.strip().split("\n")
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)
        return []

def classify_results(results):
    dns_records = []
    ip_addresses = []

    ipv4_regex = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    ipv6_regex = re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$')

    for result in results:
        if ipv4_regex.match(result) or ipv6_regex.match(result):
            ip_addresses.append(result)
        else:
            dns_records.append(result)

    return dns_records, ip_addresses

def main(target):
    domain = target
    results = run_dig(domain)
    
    if not results:
        print("No output found for the given domain.")
        return

    dns_records, ip_addresses = classify_results(results)

    if not ip_addresses and not dns_records:
        print("No IP addresses or DNS records found.")
    else:
        return dns_records, ip_addresses
