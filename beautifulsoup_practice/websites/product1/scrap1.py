# import requests
from bs4 import BeautifulSoup
import pandas as pd



with open('./product1/index.html','r',encoding='utf-8') as file:
    r = file.read()
soup = BeautifulSoup(r, 'html.parser')


data = {'Title': [], 'Description': [] , 'Price': [] , 'rating': [] , 'material': []}

title = soup.select_one("span.a-size-large.product-title-word-break").text
print(title)
data['Title'].append(title)

description = soup.select_one("div#productDescription_feature_div").text
print(description)
data['Description'].append(description)
   
price = soup.select_one("td.a-span12").text
print(price)
data['Price'].append(price)

rating = soup.select_one("span.a-icon-alt").string
print(rating)
data['rating'].append(rating)


material = soup.select_one("div.a-fixed-left-grid.product-facts-detail").text
print(material)
data['material'].append(material)

df = pd.DataFrame.from_dict(data)
df.to_csv("data.csv" , index=False)


# df = pd.DataFrame.from_dict(data, orient='index')
# df = df.transpose()