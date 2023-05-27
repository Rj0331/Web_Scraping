import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://ticker.finology.in/"

r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
#first extract the table
table = soup.find("table", class_= "table table-sm table-hover screenertable")


#from tables extract the headers with find all
headers = table.find_all("th")
items = [] #create an empty list and add all the headers in the list
for i in headers:
    item = i.text
    items.append(item)

df = pd.DataFrame(columns=items)
#print(df)
rows = table.find_all("tr")
for i in rows[1:]:
    # print(i.text)# Gives the data in the list for and for converting it into proper table form we need to perform:
    data = i.find_all("td")
    # print(data)# gives data in a list
    row = [tr.text for tr in data]
    # print(row) gives data in proper format but now we need to show it in a data frame
    l = len(df) # this will find the length of the data frame
    df.loc[l] = row # for every iteration in the loop from index 1 to last it will add the row into the data frame
print(df)
df.to_csv("Stock_Market_Data.csv") # converts the data frame to csv
