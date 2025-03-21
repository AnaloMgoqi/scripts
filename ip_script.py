#!/usr/bin/env python3
import urllib.request
import sys

def main():
    url = "https://ifconfig.me"
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            public_ip = response.read().decode('utf-8').strip()
    except Exception:
        print("Error: Unable to retrieve public IP.")
        sys.exit(1)

    if not public_ip:
        print("Error: Unable to retrieve public IP.")
        sys.exit(1)

    print("Your public IP address is:", public_ip)

if __name__ == '__main__':
    main()
