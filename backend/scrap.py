
import requests
from bs4 import BeautifulSoup
import json

# Website to scrape
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

# Extract product data
products = []
for product in soup.select(".thumbnail"):
    name = product.select_one(".title").get_text(strip=True)
    price = product.select_one(".price").get_text(strip=True)
    description = product.select_one(".description").get_text(strip=True)
    
    products.append({
        "name": name,
        "price": price,
        "description": description
    })

# Save data into JSON file
with open("products.json", "w", encoding="utf-8") as f:
    json.dump(products, f, indent=4, ensure_ascii=False)

print("Data saved to products.json")
