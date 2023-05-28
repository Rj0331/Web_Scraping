import requests
from bs4 import BeautifulSoup
import pandas as pd

Names = []
Prices = []
Desc = []
Ratings = []

for i in range(1,14):

    url = "https://www.airbnb.co.in/s/New-Delhi--India/homes?adults=1&place_id=ChIJLbZ-NFv9DDkRzk0gTkm3wlI&refinement_paths%5B%5D=%2Fhomes&checkin=2023-05-28&checkout=2023-05-29"

    r = requests.get(url)

    soup = BeautifulSoup(r.text,"html.parser")
    box = soup.find("div",class_="lwy0wad l1tup9az dir dir-ltr")

    #print(r)
    #while True:
    np = soup.find("a",class_="l1j9v1wn c1ytbx3a dir dir-ltr").get("href")
    cnp = "https://www.airbnb.co.in/" + np
    # print(cnp)

    url = cnp
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")

    name = soup.find_all("div", class_="t1jojoys dir dir-ltr")
    for i in name:
        n = i.text
        Names.append(n)
        # print(len(Names))

    price = soup.find_all("div", class_="pquyp1l dir dir-ltr")
    for i in price:
        p = i.text
        Prices.append(p)
        # print(len(Prices))


    des = soup.find_all("span", class_="t6mzqp7 dir dir-ltr")
    for i in des:
        d = i.text
        Desc.append(d)
        # print(len(Desc))


    # rat = soup.find_all("span", class_="t5eq1io r4a59j5 dir dir-ltr")
    # for i in rat:
    #     r = i.text
    #     Ratings.append(r)
    #     # print(len(Ratings))
    # There were some stays with no reviews, Array length could no match, Excluding the reviews part from the data frame

df = pd.DataFrame({"Names ": Names, "Prices ": Prices, "Description ":Desc})
# print(df)
df.to_csv("AirBnb_Delhi_Stays.csv")
