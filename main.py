import requests
import json
from pathlib import Path
import pandas as pd
import sqlite3

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

# Step 3: Filter top 5 products by rating
def get_top5_products(json_path):
    print("Filtering top 5 products by rating...")
    # Load JSON data
    with open(json_path, "r") as f:
        data = json.load(f)
    # Normalize JSON to flat table
    df = pd.json_normalize(data)
    # Sort by rating.rate descending
    df_top5 = df.sort_values(by="rating.rate", ascending=False).head(5)
    print("Top 5 products selected.")
    return df_top5

# Step 4: Save data to SQLite
def save_to_sqlite(df, db_path, table_name="products"):
    print(f"Saving data to SQLite DB: {db_path}...")
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    print("Data saved to SQLite.")

if __name__ == "__main__":
    # Ensure data folder exists
    Path("data").mkdir(exist_ok=True)

    products = fetch_data(API_URL)
    save_raw_data(products, "data/raw.json")

    top5_df = get_top5_products("data/raw.json")
    print(top5_df[["title", "price", "rating.rate"]])  # Preview

    # Save full dataset to SQLite
    df_all = pd.json_normalize(products)  # Normalize JSON to flat table
    save_to_sqlite(df_all, "data/products.db")
    # Save top 5 products to a CSV
    top5_df.to_csv("data/top5_products.csv", index=False)
    print("Top 5 products saved to CSV.")

    # Save top 5 products to SQLite
    save_to_sqlite(top5_df, "data/top5_products.sqlite", table_name="top5_products")
    print("Top 5 products saved to SQLite.")