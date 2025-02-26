# Scrape Website: https://shop.parmigianoreggiano.com

# Import Libraries
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

master_list = []

def get_info(page_number):

  url = f"https://shop.parmigianoreggiano.com/it/shop.html?p={page_number}" 

  html = requests.get(url).text 
  soup = bs(html, "html.parser")

  products = soup.find_all("li", {"class": "item product product-item"})
  
  for product in products: 
    company_name = product.find("a", {"class": "nome-caseificio"}).text


    p_name = product.find("a", {"class": "product-item-link"})
    if p_name is not None:
      product_name = p_name.text

 
    p_per_kg = product.find("div", {"class": "info-wrapper"}).find("span", {"class": "prezzo-kg"})
    if p_per_kg is not None:
      price_per_kg = p_per_kg.text

    price = product.find("span", {"class": "price"}).text

    weight = product.find("span", {"class": "formato-peso"}).text

    product_info = {
      "Company Name": company_name,
      "Product Name": product_name,
      "Price Per Kg": price_per_kg,
      "Price": price,
      "Weight": weight
    }

    master_list.append(product_info)

  df = pd.DataFrame(master_list)
  df.to_csv("shop.csv", index=False)

  df = pd.DataFrame(master_list)
  df.to_excel("shop.xlsx", index=False)

  df = pd.DataFrame(master_list)
  df.to_txt("shop.txt", index=False)

for page_number in range(1, 100): # Feel free to customize the range according to your needs; for instance, you can set it to range(1, 1000) or adjust it as per your preference    
  get_info(page_number)
print("File Created.")




   






 
