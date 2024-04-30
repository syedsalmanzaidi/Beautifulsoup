from bs4 import BeautifulSoup
import pandas as pd

# url = "https://www.etsy.com/listing/244810634/classic-gold-stackable-rings-14k-gold?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=sc_gallery-1-2&pro=1&sts=1&plkey=c07322d73889de77df272bffd9d547ad2daacb82%3A244810634"
with open("./product4/index.html" , 'r' , encoding="utf-8") as f:
    r = f.read()
soup = BeautifulSoup(r, 'html.parser')
data = {'title': [], 'price': [] , 'descriotn': []}

title = soup.select_one("h1.wt-text-body-01.wt-line-height-tight.wt-break-word.wt-mt-xs-1").text
# print(title)
data['title'].append(title)

price = soup.select_one("p.wt-text-title-larger.wt-mr-xs-1.wt-text-slime ").text
print(price)
data['price'].append(price)


descriotn = soup.select_one("div.reviews__shop-info").text
# print(review)
data['descriotn'].append(descriotn)


df = pd.DataFrame.from_dict(data)
df.to_csv("data.csv" , index=False)

