import requests
from bs4 import BeautifulSoup
import pandas as pd
data = {'Pages': [], 'Size': [] , 'Language': [] }


# url = "https://www.libgen.is/search.php?&req=fiction&phrase=1&view=simple&column=def&sort=def&sortmode=ASC&page=1"
# r = requests.get(url )

with open("./Libgin_library_books/index1.html" , 'r' , encoding='utf-8')  as f:
    r = f.read()
soup = BeautifulSoup(r, 'html.parser')
with open("./Libgin_library_books/tset.html" , 'r' , encoding='utf-8')  as file:
    r2 = file.read()
soup2 = BeautifulSoup(r2, 'html.parser')

# author = []
# new=[]
# author = soup.find_all("a")
# for i in author:
#     href = i.get("href" , '')
#     if(href.endswith("=author")):
#         author.append(i.text)
#         if(i.text == ""):
#             (author.append("NO Author"))
# print(author)

# ID
# ID = []
# ids = soup.find_all('a')
# for i in ids:
#     id=i.get('id' , '')
#     (ID.append(id))
# for j in ID:
#     print(j  , end=' ')

# Title
# title = soup2.find_all('a')
# for i in title:
#     text = ''.join(i.find_all(text=True, recursive=False)).strip()
#     # print(text)
#     if "<font" in text:
#         text = text.split('<font')[0]
#     if "<i>" in text:
#         text = text.split('<i>')[0]
#     print(text.strip())
# print(text)


# Year
# year = soup.find_all("td" , nowrap='')
# new_year=[]
# # print(year)
# for i in year:
#     text = ''.join(i.find_all(text=True, recursive=False)).strip()

#     if len(text) == 4:
#         new_year.append(text)
# new = []
# for i in new_year:
#     x = i.replace(" " , "")
#     new.append(x)

# now = []

# for i in new:     
#     if("2Mb" in i):       
#         print(i.replace("2Mb" , ''))
#     elif("1Mb" in i):
#         print(i.replace("1Mb" , ''))
#     elif("3Mb" in i):
#         print(i.replace("3Mb" , ''))
#     elif("4Mb" in i):
#         print(i.replace("4Mb" , ''))
#     elif("djvu" in i):
#         print(i.replace("djvu" , ''))
#     else:     
#         now.append(i)
# print(now , len(now))


# Pages
page = []
new_page = []

td_tags = soup.find_all('td')
for i in td_tags:
    text = i.get_text(strip=True)
    if text:
        page.append(text)
for value in page:
    # print(value , len(value))
    if((len(value) == 3 or len(value) == 1) and   (value.startswith("0") or  value.startswith("1") or value.startswith("2")  or value.startswith("3") or value.startswith("4") or value.startswith("5") or value.startswith("6") or value.startswith("7") or value.startswith("8") or value.startswith("9"))):
        print(value)
        new_page.append(value)
data['Pages'].append(new_page)

# Size
size = []
new_size = []
s = soup.find_all("td" , nowrap='')
for i in s:
    si = ''.join(i.find_all(text=True, recursive=False)).strip()
    # print(si)
    if "Mb" in si or 'Kb' in si:
        size.append(si)

for i in size:
    if("Mb" in i or  'Kb' in i):
        new_size.append(i)

print(new_size , len(new_size))
data['Size'].append(new_size)



# Language
language = []
lang = soup.find_all("td" , nowrap=False)
for i in lang:
    if("Russian" in i or "English" in i or "German" in i):
        language.append(i.text)
print(language )
data['Language'].append(language)



# # Publisher
# pub = soup.find_all("td" , nowrap=False )
# for  i in pub:
#     a = (i.get_text())
#     if(len(a) > 5):
#         print(a)




df = pd.DataFrame.from_dict(data)
df.to_csv("./Libgin_library_books/books.csv" , index=False)