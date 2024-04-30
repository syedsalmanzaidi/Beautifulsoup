from bs4 import BeautifulSoup
import pandas as pd
# url = "https://www.ebay.com/itm/176028954927?_trkparms=amclksrc%3DITM%26aid%3D777008%26algo%3DPERSONAL.TOPIC%26ao%3D1%26asc%3D20240114230122%26meid%3D619986e3328e43b5ac5f120b9ddc394f%26pid%3D101950%26rk%3D1%26rkt%3D1%26itm%3D176028954927%26pmt%3D0%26noa%3D1%26pg%3D4375194%26algv%3DFeaturedDealsV2&_trksid=p4375194.c101950.m162919&_trkparms=parentrq%3A748e765618e0ab8e4fff0ff0fffd9a8c%7Cpageci%3A107eb3c7-ea7b-11ee-8cbe-f62fcc33df51%7Ciid%3A1%7Cvlpname%3Avlp_homepage"
with open("./product3/index3.html" , 'r' , encoding="utf-8") as f:
    r = f.read()
soup = BeautifulSoup(r, 'html.parser')
data = {'title': [], 'price': [] , 'description': [] , 'delivery': [] , 'brand': [] , 'OS': [] , 'GPU': [] , 'brand_size': []}



title = soup.select_one("h1.x-item-title__mainTitle").text
print(title)
data['title'].append(title)

price = soup.select_one("div.x-price-primary").text
# print(price)
data['price'].append(price)

description = soup.select_one("div.ux-labels-values-with-hints.ux-labels-values-with-hints--SECONDARY-SMALL").text
# print(shiping)
data['description'].append(description)

delivery = soup.select_one("div.vim.ux-labels-values-with-custom-help").text
# print(delivery)
data['delivery'].append(delivery)

brand = soup.select_one("dl.ux-labels-values.ux-labels-values--inline.col-6.ux-labels-values--brand").text
# print(brand)
data['brand'].append(brand)

OS = soup.select_one("dl.ux-labels-values.ux-labels-values--inline.col-6.ux-labels-values--operatingSystem").text
# print(OS)
data['OS'].append(OS)

GPU = soup.select_one("dl.ux-labels-values.ux-labels-values--inline.col-6.ux-labels-values--gpu").text
# print(GPU)
data['GPU'].append(GPU)

brand_size = soup.select_one("dl.ux-labels-values.ux-labels-values--inline.col-6.ux-labels-values--ramSize").text
# print(brand_size)
data['brand_size'].append(brand_size)

df = pd.DataFrame.from_dict(data)
df.to_csv("data.csv" , index=True)
