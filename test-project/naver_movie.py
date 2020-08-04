import requests
from bs4 import BeautifulSoup
import csv


url = "https://movie.naver.com/movie/running/current.nhn"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

movie_selection = soup.select('div[id=content] > div.article > div.obj_section > div.lst_wrap > ul.lst_detail_t1 > li')

movie_data = []

for movie in movie_selection:
    
    a_tag = movie.select_one('dl > dt > a')
    
    movie_title = a_tag.text
    movie_code = a_tag['href'].split('=')[1]


    movie_dict = {
        'title': movie_title,
        'code': movie_code
    }
    
    movie_data.append(movie_dict)
 

print(movie_data)


with open('./data/naver_movie.csv', 'w') as csvfile:
    filednames = ['title', 'code']
    writer = csv.DictWriter(csvfile, fieldnames=filednames, lineterminator = '\n')
    writer.writeheader()
    writer.writerows(movie_data)


