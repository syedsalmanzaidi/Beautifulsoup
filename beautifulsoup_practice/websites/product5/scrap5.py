from bs4 import BeautifulSoup
import pandas as pd

# url = "https://www.amazon.co.uk/VXDAS-Scanner-Diagnostic-Engine-Universal/dp/B083W1LGDP?pf_rd_r=M9FSXDA9ZJ2P79WAH81K&pf_rd_t=Events&pf_rd_i=springdealdays&pf_rd_p=66770517-6f66-451e-a3fe-f80329f519db&pf_rd_s=slot-6&ref=dlx_sprin_gd_dcl_img_20_fb949e35_dt_sl6_db"

with open("./product5/index.html" , 'r' , encoding="utf-8") as f:
    r = f.read()
soup = BeautifulSoup(r, 'html.parser')
data = {'title': [], 'description': [] , 'price': [] , 'brand': [] }

title = soup.select_one("span.a-size-large.product-title-word-break").text
data['title'].append(title)


description = soup.select_one("div.a-section.launchpad-text-left-justify").text
data['description'].append(description)

price = soup.select_one("span.a-offscreen").text
data['price'].append(price)

brand = soup.select_one("span.a-size-base.po-break-word").text
data['brand'].append(brand)

df = pd.DataFrame.from_dict(data)
df.to_csv("data.csv" , index=False)

