import requests
from bs4 import BeautifulSoup



response = requests.get(url="https://news.ycombinator.com/")

response.raise_for_status()
html_string = response.text

soup = BeautifulSoup(html_string,"html.parser")
# a_tag = soup.find(name="span", class_="titleline")

table_row = soup.select(selector="tr")
name=[]
upvotes_list=[]
link_list = []
for table in table_row:
    title = table.find(name="span" ,class_="titleline")
    votes = table.find(name="span",class_="score")
    
    if title is not None:
        individual_title = title.find(name = "a")
        link = individual_title.get("href")
        # print("link:",link)
        name.append(individual_title.getText())
        link_list.append(link)
        # print("title_name:",individual_title.getText())

        pass
    elif votes is not None:
        upvotes = votes.getText()
        upvotes_list.append(upvotes)
        # print("upvotes:",upvotes)
        # print("\n\n\n\n")

    else:
        pass

# print(name)
# print(link_list)
# print(upvotes_list)
vote_list = []
for votes in upvotes_list:
    v=int(votes.split()[0])
    vote_list.append(v)
    
    
largest = max(vote_list)

index_largest=vote_list.index(largest)

print(f"{name[index_largest]},{link_list[index_largest]},{largest}")



    # print(title)
# print(a_tag)
# for a in a_tag:
    
#     a_tag_link = a.get("href")
#     a_tag_upvote =  soup.select(selector="tr td span.subline span.score")


#     print("link",a_tag_link)
#     print("points",a_tag_upvote.text)

