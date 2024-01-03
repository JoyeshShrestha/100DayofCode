import requests
from bs4 import BeautifulSoup
response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_html = response.text


movie = BeautifulSoup(movie_html,"html.parser")

movie_title = movie.find_all(name="h3",class_="title")

title = [movie.getText() for movie in movie_title]
title.reverse()
print(title)


with open("movies.txt","w",errors='replace') as file:
        for m in title:
            file.write(f"{m}\n")

    
  
