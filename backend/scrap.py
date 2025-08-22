# import os
# import requests
# from bs4 import BeautifulSoup
# import csv
# import pandas as pd

# url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
# r = requests.get(url)

# soup = BeautifulSoup(r.text, "lxml")

# # Extract names
# names = soup.find_all("a", class_="title")
# # Extract prices
# prices = soup.find_all("h4", class_="price float-end card-title pull-right")


# # Open CSV file to write
# with open("products.csv", "w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Price"])  # header row

#     # Write data row by row
#     for name, price in zip(names, prices):
#         writer.writerow([name.text.strip(), price.text.strip()])
   
# print("✅ Data saved to products.csv")

# df = pd.read_csv("products.csv")
# print(df)

# df.to_csv("D:/scraped data/scrapded_data.csv")





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
