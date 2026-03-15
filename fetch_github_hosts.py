import requests
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Try to fetch latest github hosts
url = "https://raw.githubusercontent.com/maxiaof/github-hosts/master/hosts"
try:
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        print("Successfully fetched latest GitHub hosts:")
        print("-" * 50)
        # Filter github related lines
        for line in response.text.split('\n'):
            if line.strip() and not line.startswith('#') and 'github' in line.lower():
                print(line.strip())
        print("-" * 50)
        with open('latest_github_hosts.txt', 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f"\nSaved to: latest_github_hosts.txt")
    else:
        print(f"Failed to fetch: status code {response.status_code}")
except Exception as e:
    print(f"Error: {e}")
