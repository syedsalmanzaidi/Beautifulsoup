from bs4 import BeautifulSoup
import pandas as pd

data = {'title': [], 'Description': [] , 'price': [] }

with open('index0.html','r',encoding='utf-8') as file:
    r0 = file.read()
with open('index1.html','r',encoding='utf-8') as file:
    r1 = file.read()
with open('index2.html','r',encoding='utf-8') as file:
    r2 = file.read()
with open('index3.html','r',encoding='utf-8') as file:
    r3 = file.read()
with open('index4.html','r',encoding='utf-8') as file:
    r4 = file.read()
with open('index5.html','r',encoding='utf-8') as file:
    r5 = file.read()


soup0 = BeautifulSoup(r0, 'html.parser')
soup1 = BeautifulSoup(r1, 'html.parser')
soup2 = BeautifulSoup(r2, 'html.parser')
soup3 = BeautifulSoup(r3, 'html.parser')
soup4 = BeautifulSoup(r4, 'html.parser')
soup5 = BeautifulSoup(r5, 'html.parser')


#Titles
title = soup0.select_one("span.a-size-large.product-title-word-break").text
data['title'].append(title)
title = soup1.select_one("span.a-size-large.product-title-word-break").text
data['title'].append(title)
title = soup2.select_one("h1.x-item-title__mainTitle").text
data['title'].append(title)
title = soup3.select_one("h1.x-item-title__mainTitle").text
data['title'].append(title)
title = soup4.select_one("h1.wt-text-body-01.wt-line-height-tight.wt-break-word.wt-mt-xs-1").text
data['title'].append(title)
title = soup5.select_one("span.a-size-large.product-title-word-break").text
data['title'].append(title)


# Description
Description = soup0.select_one("div.a-row.feature").text
data['Description'].append(Description)
Description = soup1.select_one("div#productDescription_feature_div").text
print(Description)
data['Description'].append(Description)
Description = soup2.select_one("dl.ux-labels-values.ux-labels-values--inline.col-6.ux-labels-values--boardMaterial").text
data['Description'].append(Description)
Description = soup3.select_one("div.ux-labels-values-with-hints.ux-labels-values-with-hints--SECONDARY-SMALL").text
data['Description'].append(Description)
Description = soup4.select_one("div.reviews__shop-info").text
data['Description'].append(Description)
Description = soup5.select_one("div.a-section.launchpad-text-left-justify").text
data['Description'].append(Description)



# price
price = soup0.select_one("span.a-price-whole").text
data['price'].append(price)
price = soup1.select_one("td.a-span12").text
data['price'].append(price)
price = soup2.select_one("div.x-price-primary").text
data['price'].append(price)
price = soup3.select_one("div.x-price-primary").text
data['price'].append(price)
price = soup4.select_one("p.wt-text-title-larger.wt-mr-xs-1.wt-text-slime ").text
data['price'].append(price)
price = soup5.select_one("span.a-offscreen").text
data['price'].append(price)




df = pd.DataFrame.from_dict(data)
df.to_csv("data.csv" , index=False)

