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
 

# print(movie_data)


# with open('./data/naver_movie.csv', 'w') as csvfile:
#     filednames = ['title', 'code']
#     writer = csv.DictWriter(csvfile, fieldnames=filednames, lineterminator = '\n')
#     writer.writeheader()
#     writer.writerows(movie_data)



movie_reviews = []
for movie in movie_data:
   
    params = (
        ('code', movie['code']),
        ('type', 'after'),
        ('isActualPointWriteExecute', 'false'),
        ('isMileageSubscriptionAlready', 'false'),
        ('isMileageSubscriptionReject', 'false'),
    )

    response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', params=params)

    soup = BeautifulSoup(response.text, 'html.parser')

    reviews = soup.select('body > div > div > div.score_result > ul > li')
    count = 0

    
    for review in reviews:
        review_dict = {}
        star_score = review.select_one('div.star_score > em').text
        if not review.select(f'div.score_reple > p > span#_filtered_ment_{count} > span#_unfold_ment{count} > a'): 
            reple = review.select_one(f'div.score_reple > p > span#_filtered_ment_{count}').text.strip()
        else:
            reple = review.select_one(f'div.score_reple > p > span#_filtered_ment_{count} > span#_unfold_ment{count} > a')['data-src']
        
        count += 1

        review_dict['title'] = movie['title']
        review_dict['code'] = movie['code']
        review_dict['star_score'] = star_score
        review_dict['reple'] = reple
        movie_reviews.append(review_dict)


with open('./data/naver_movie_reviews.csv', 'w') as csvfile:
    filednames = ['title', 'code', 'star_score', 'reple']
    writer = csv.DictWriter(csvfile, fieldnames=filednames, lineterminator='\n')
    writer.writeheader()
    writer.writerows(movie_reviews)



    

        

        





