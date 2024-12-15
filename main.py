import requests

# Vulnerability: Hardcoded secret (Triggers secrets detection)
API_KEY = "12345-ABCDEF-SECRET"

def fetch_data(url):
    # Vulnerability: Hardcoded sensitive data (Triggers secrets detection)
    headers = {"Authorization": f"Bearer {API_KEY}"}

    # Vulnerability: Using requests without verifying SSL (Triggers dependency scanning)
    response = requests.get(url, headers=headers, verify=False)

    if response.status_code == 200:
        return response.json()
    else:
        # Vulnerability: Weak error handling (May trigger SAST if flagged by CodeQL)
        print("Failed to fetch data:", response.status_code)
        return None

def main():
    # Vulnerability: Hardcoded URL (May trigger SAST depending on the tool's rules)
    url = "https://example.com/api/data"

    # Vulnerability: Insecure direct object reference (IDOR)
    data = fetch_data(url + "?id=1")

    # Output fetched data
    if data:
        print("Fetched Data:", data)

if __name__ == "__main__":
    main()