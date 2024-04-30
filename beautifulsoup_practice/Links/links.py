from bs4 import BeautifulSoup
 
with open("./Links/index.html" , 'r' , encoding='utf-8') as f:
    r = f.read()
soup = BeautifulSoup(r, 'html.parser')

pants = soup.find_all('a' )

product_links=[]
nn=[]
remove_duplicate=[]

for i in pants:
    href = i.get('href', '')
    if( href.startswith('/products')):
        product_links.append(href)
for link in product_links:
    new_link=f"https://kidoriman.com/{link}"
    nn.append(new_link)
# print(nn)
for remove in nn:
    if(remove not in remove_duplicate):
        remove_duplicate.append(remove)
# print(remove_duplicate)


with open('./Links/test.html','w') as file:
    file.write('\n'.join(remove_duplicate))
