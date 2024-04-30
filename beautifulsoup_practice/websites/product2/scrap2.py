from bs4 import BeautifulSoup
import pandas as pd

with open("./product2/index2.html" , 'r' ,encoding='utf-8') as file:
    r = file.read()
soup = BeautifulSoup(r, 'html.parser')

data = {'Title': [], 'Price': [] , 'condition': [] , 'delivery': [] , 'description': [] , 'Model': [] , 'size': [] , 'MPN': []}


title = soup.select_one("h1.x-item-title__mainTitle").text
print(title)
data['Title'].append(title)

price = soup.select_one("div.x-price-primary").text
# print(price)
data['Price'].append(price)

condition = soup.select_one("div.ux-layout-section-evo__col").text
# print(condition)
data['condition'].append(condition)

delivery = soup.select_one("div.ux-labels-values.col-12.ux-labels-values__column-last-row.ux-labels-values--deliverto").text
# print(delivery)
data['delivery'].append(delivery)

description = soup.select_one("dl.ux-labels-values.ux-labels-values--inline.col-6.ux-labels-values--boardMaterial").text
# print(Material)
data['description'].append(description)

Model = soup.select_one("dl.ux-labels-values.ux-labels-values--inline.col-6.ux-labels-values--model").text
# print(Model)
data['Model'].append(Model)

size = soup.select_one("dl.ux-labels-values.ux-labels-values--inline.col-6.ux-labels-values--boardSize").text
# print(size)
data['size'].append(size)

MPN = soup.select_one("dl.ux-labels-values.ux-labels-values--inline.col-6.ux-labels-values__column-last-row.ux-labels-values--mpn").text
# print(MPN)
data['MPN'].append(MPN)

df = pd.DataFrame.from_dict(data)
df.to_csv("data.csv" , index=False)
