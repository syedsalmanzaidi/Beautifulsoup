import requests
from bs4 import BeautifulSoup

with open("sample.html","r") as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())
# print(soup.title.parent.name)

# for link in soup.find_all("a"):
#     print(link)

# for child in soup.find(class_='container').children:
#     print(child)
# for parent in soup.find(class_="box").parents:
#     print(parent)


# count = soup.find(class_="container")
# print(count)
# count.name="span"
# count['class']="class2"
# count.string="I am not a box"
# print(count)

# ultag=soup.new_tag("ul")

# litag=soup.new_tag("li")
# litag.string="Home"
# ultag.append(litag)

# litag=soup.new_tag("li")
# litag.string="About"
# ultag.append(litag)

# soup.html.body.insert(0 , ultag)
# with open("modified.html" , 'w') as f:
#     f.write(str(soup))


# cont = soup.find(class_="container")
# print(cont.has_attr("class"))


def class_but_not_id(tag):
    return tag.has_attr("class") and not tag.has_attr("id")
result = soup.find_all(class_but_not_id)
for results in result:
        print(results, "\n")

# def content(tag):
#     return tag.has_attr("content")
# result = soup.find_all(content)
# for results in result:
#         print(results, "\n\n")