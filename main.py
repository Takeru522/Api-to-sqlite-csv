import requests
import json
from pathlib import Path

# Step 1: Fetch data from the fake API
API_URL = "https://fakestoreapi.com/products"

def fetch_data(api_url):
    print("Fetching data from API...")
    response = requests.get(api_url)
    response.raise_for_status()  # Raises error if response is bad
    data = response.json()
    print(f"Fetched {len(data)} items.")
    return data

# Step 2: Save raw data to a file (optional but useful)
def save_raw_data(data, filepath):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Raw data saved to {filepath}")

# Make sure data folder exists
Path("data").mkdir(exist_ok=True)

if __name__ == "__main__":
    products = fetch_data(API_URL)
    save_raw_data(products, "data/raw.json")