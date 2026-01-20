import json
import requests
from pprint import pprint

def main():
    # Example: fetch a simple JSON response
    resp = requests.get("https://api.github.com")
    resp.raise_for_status()
    data = resp.json()

    print("Top-level keys:")
    pprint(list(data.keys()))

    # Example: use json module explicitly
    as_text = json.dumps(data, indent=2)
    print("\nJSON preview:")
    print(as_text[:300])

if __name__ == "__main__":
    main()
