import requests
import pandas as pd
from bs4 import BeautifulSoup

Names = []
Prices = []
Desc = []
Reviews = []


for i in range(1,11):
    url ="https://www.flipkart.com/search?q=mobiles+under+50000&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_5_0_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_5_0_na_na_na&as-pos=5&as-type=HISTORY&suggestionId=mobiles+under+50000&requestId=331479a9-8c85-42a9-9487-59669a846453&page=" + str(i)

    r = requests.get(url)
    # print(r)
    soup = BeautifulSoup(r.text, "html.parser")
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")
    names = box.find_all("div", class_="_4rR01T") # As the number of reviews were greater than the other arrays, choose the part where only that particular flex was applicable
    for i in names:
        n = i.text
        Names.append(n)
    # print(len(Names))

    prices = box.find_all("div", class_= "_30jeq3 _1_WHN1")
    for i in prices:
        p = i.text
        Prices.append(p)
    # print(len(Prices))

    desc = box.find_all("div", class_= "fMghEO")
    for i in desc:
        d = i.text
        Desc.append(d)
    # print(len(Desc))

    rev = box.find_all("span",class_= "_2_R_DZ")
    for i in rev:
        r = i.text
        Reviews.append(r)
    # print(len(Reviews))
df = pd.DataFrame({"Product Name ": Names, "Product Price ": Prices, "Product Description ": Desc, "Product Reviews ": Reviews })
print(df)
df.to_csv("Flipkart Scrape.csv")
# Creating a goto next page link when there are different links for pages
# while True:
# np = soup.find("a",class_="_1LKTO3").get("href") # this variable get the link from the html source of the next page
# cnp = "https://www.flipkart.com" + np  # completed the next page link by adding the host name i.e. flipkart.com
# print(cnp)

# to continue to get next page links , make the cnp as the next url
# The below lines work for the websites which have different url in the next pages
# url = cnp
# r = requests.get(url)
# soup = BeautifulSoup(r.text, "html.parser")
# To add specific page numbers to new urls we will be using for loop as shown below
