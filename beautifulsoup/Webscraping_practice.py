import requests
from bs4 import BeautifulSoup
import pandas as pd


 
data = {'title': [], 'price': []}
url = "https://www.amazon.co.uk/s?k=iphone&ref=nb_sb_noss"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url , headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")
for span in spans:
    print(span.string)
    data['title'].append(span.string)

price=soup.select("div.a-section.a-spacing-none.a-spacing-top-micro.puis-price-instructions-style")
for prices in price:
    print(prices.get_text())
    data['price'].append(prices.get_text())


df = pd.DataFrame.from_dict(data)
df.to_csv("data.csv" , index=False)