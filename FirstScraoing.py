import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyexcel



url = "https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url) # gets the url
#print(r.text)

soup = BeautifulSoup(r.text, "html.parser")
prices = soup.find_all("h4", class_="pull-right price")
product_price = []
for i in prices:
    price = i.text
    product_price.append(price)

# print(product_price)

names = soup.find_all("a", class_="title")
product_name = []
for i in names:
    name = i.text # converts the name format into text
    product_name.append(name) # adds the various names in the empty list created above
# print(product_name)

desc = soup.find_all("p", class_="description") # finds all the descriptions in the website
product_desc = [] # is an empty list created to store the desc of products
for i in desc:
    des = i.text
    product_desc.append(des)
# print(product_desc)

# Exporting the datas extracted in a proper format using dataframes in the pandas library
df = pd.DataFrame({"Product Name": product_name, "Product Price": product_price, "Product Description" : product_desc})
# print(df)

# Converting the dataframe to csv file
df.to_csv("Product Details.csv")
