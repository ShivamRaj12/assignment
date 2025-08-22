# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# # Allow frontend (Vite React) to call backend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/")
# def read_root():
#     return {"message": "Hello from Python backend"}

# @app.get("/api/data")
# def get_data():
#     return {"products": ["Shirt", "Jeans", "shoes"]}


# server/main.py





# from fastapi import FastAPI
# import requests
# from bs4 import BeautifulSoup

# app = FastAPI()

# @app.get("/scrape")
# def scrape_quotes():
#     url = ""
#     res = requests.get(url)
#     soup = BeautifulSoup(res.text, "html.parser")

#     quotes = []
#     for q in soup.select(".quote"):
#         quotes.append({
#             "text": q.select_one(".text").get_text(),
#             "author": q.select_one(".author").get_text(),
#             "tags": [t.get_text() for t in q.select(".tags .tag")]
#         })

#     return {"quotes": quotes}









from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# Allow frontend (React) to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/products")
def get_products():
    url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    products = []

    items = soup.find_all("div", class_="col-sm-4 col-lg-4 col-md-4")

    for item in items:
        name = item.find("a", class_="title").text.strip()
        price = item.find("h4", class_="pull-right price").text.strip()
        desc = item.find("p", class_="description").text.strip()

        products.append({
            "name": name,
            "price": price,
            "description": desc
        })

    return {"products": products}





