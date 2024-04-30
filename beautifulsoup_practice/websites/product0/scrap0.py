# import requests
from bs4 import BeautifulSoup
import pandas as pd

#url = "https://www.amazon.co.uk/12-Smartphone-Unlocked-Original-Packaging-White/dp/B0CY2Z8V1P/ref=sr_1_3?dib=eyJ2IjoiMSJ9.hA-h2fPwEYLqs1TYrkQGUcZi4iW03IAvKTua25o6PrMPIBLpVsONBYkML9zhP-fDtlNbDOYCBSw58VlgY0ssMc_ZOHrZDEnlO_lDTdrTbUotq4z27fsOJhRBc4KNSCY0di78QoHux7UQwKMK3-wGwy3J_1BjQTOivIfL3p9lwHBbP-TtrirKFxF2xM5nJN2gKeFroyBKkUMvuJ_YZOclPtIm59zsxl9GEOFLD0ZyZcw.GbT91J0fb1I2c_ot6oP6XXga4vu2okgnMH7CRCkcCc0&dib_tag=se&keywords=iphone&qid=1711187400&sr=8-3"
#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

#r = requests.get(url  , headers=headers)
with open('test.html','r',encoding='utf-8') as file:
    r = file.read()
soup = BeautifulSoup(r, 'html.parser')

data = {'Title': [], 'Description': [] , 'Price': [] , 'Brand': [] , 'Model': [] , 'Memory': [] , 'Color': [] , 'Component': []}




title = soup.select("span.a-size-large.product-title-word-break")
for titles in title:
    print(titles.string)
    data['Title'].append(titles.string)
 

desc = soup.select("div.a-row.feature")
for i in desc:
    print(i.text)
    data['Description'].append(i.text)


price = soup.select_one("span.a-price-whole").text


brand = soup.select("a#bylineInfo").text

model=soup.select("tr.a-spacing-small.po-model_name")
for models in model:
    print(models.text)
    data['Model'].append(models.text)

memory=soup.select("tr.a-spacing-small.po-memory_storage_capacity")
for m in memory:
    print(m.text)
    data['Memory'].append(m.text)

color = soup.select("tr.a-spacing-small.po-color")
for colors in color:
    print(colors.text)
    data['Color'].append(colors.text)

component = soup.select("tr.a-spacing-small.po-included_components")
for i in component:
    print(i.text)
    data['Component'].append(i.text)

df = pd.DataFrame.from_dict(data)
df.to_csv("data.csv" , index=False)