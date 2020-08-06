
import requests
from bs4 import BeautifulSoup





params = (
    ('code', '188909'),
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
    star_score = review.select_one('div.star_score > em').text

    if not review.select(f'div.score_reple > p > span#_filtered_ment_{count} > span#_unfold_ment{count} > a'): 
        reple = review.select_one(f'div.score_reple > p > span#_filtered_ment_{count}').text.strip()
    else:
        reple = review.select_one(f'div.score_reple > p > span#_filtered_ment_{count} > span#_unfold_ment{count} > a')['data-src']

        
    
    # try:
    #     reple = reple.select_one('span._unfold_ment').text.strip()
    # except:
    #     reple = reple.text.strip()

    print(star_score, reple, '\n')
    count += 1