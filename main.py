from bs4 import BeautifulSoup
import pandas as pd
import requests
import numpy as np

Product_name = []
Price = []
Description = []
Reviews = []

for i in range(2,10):
    url="https://www.flipkart.com/search?q=mobilephone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

    r = requests.get(url)

    soup = BeautifulSoup(r.text,'lxml')
    box = soup.find("div",class_="_1YokD2 _3Mn1Gg")



    names = box.find_all("div",class_="_4rR01T")
    for i in names:
        name = i.text
        Product_name.append(name)
        
    # print(Product_name)

    prices = box.find_all("div",class_="_30jeq3 _1_WHN1")
    for j in prices:
        price = j.text
        Price.append(price)
    # print(Price)

    desc = box.find_all("div",class_="fMghEO")
    for k in desc:
        descs = k.text
        Description.append(descs)
    # print(Description)

    rev = box.find_all("div",class_="_3LWZlK")
    for l in rev:
        revi = l.text
        Reviews.append(revi)    
# print(Reviews)


df = pd.DataFrame({"Product Name":Product_name,"Prices":Price,"Description":Description,"Reviews":Reviews})

df.to_csv("/home/hardik/WS/Beautiful soup/amazon_data/filpcart.csv")
print("saved successfully")


    # np = soup.find("a",class_="_1LKTO3").get("href")
    # company_name = "https://www.flipkart.com"+np
    # print(company_name)
    
#---- If url name are dfferent -----
# while True:
#     np = soup.find("a",class_="_1LKTO3").get("href")
#     company_name = "https://www.flipkart.com"+np
#     print(company_name)

#     url = company_name
#     r = requests.get(url)
#     soup =BeautifulSoup(r.text,'lxml')