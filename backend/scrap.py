# import requests
# from bs4 import BeautifulSoup

# url ="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
# r = requests.get(url)
# # print(r)

# soup = BeautifulSoup(r.text, "lxml")
# # print(soup)

# names = soup.find_all("a", class_="title")

# for i in names:
#     print(i.text)

# prices = soup.find_all("h4", class_="price float-end card-title pull-right")
# for i in prices:
#     print(i.text)


import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

# Extract names
names = soup.find_all("a", class_="title")
# Extract prices
prices = soup.find_all("h4", class_="price float-end card-title pull-right")

# Open CSV file to write
with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Price"])  # header row

    

    # Write data row by row
    for name, price in zip(names, prices):
        writer.writerow([name.text.strip(), price.text.strip()])
   
print("✅ Data saved to products.csv")

df = pd.read_csv("products.csv")
print(df)

df.to_csv("D:/scraped data/scrapded_data.csv")
