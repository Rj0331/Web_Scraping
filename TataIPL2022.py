import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.iplt20.com/auction"

r = requests.get(url)
#print(r)
soup = BeautifulSoup(r.text,"html.parser")

table = soup.find("table", class_ ="ih-td-tab auction-tbl")
headers = table.find_all("th")
heads = []
for i in headers:
    head = i.text
    heads.append(head)

df = pd.DataFrame(columns=heads)
#print(df)
rows = table.find_all("tr")
for i in rows [1:]:
    data = i.find_all("td")
    row = [tr.text for tr in data]
    l = len(df)
    df.loc[l] = row
print(df)
df.to_csv("IPL_Data.csv")
