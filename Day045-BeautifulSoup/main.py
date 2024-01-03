from bs4 import BeautifulSoup

with open("C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day045-BeautifulSoup\\website.html",encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents,"html.parser")

# print(soup.title)
# print(soup.title.string)

heading = soup.find(name="h1",id="name")

print(heading.getText())

section_heading = soup.find(name="h3", class_="heading")


company_url = soup.select_one(selector="#name")

print(company_url)

