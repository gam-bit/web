# -*- encoding: utf-8 -*-
import csv
import requests
from bs4 import BeautifulSoup


def get_news_soup_objects(search_input):

    soup_objects = []

    for i in range(1, 102, 10):
        url_base = f"https://search.naver.com/search.naver?&where=news&query={search_input}&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=32&start="
        start_num = i
        url_end = "&refresh_start=0"

        url = url_base + str(start_num) + url_end

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        soup_objects.append(soup)

    return soup_objects




def get_title_and_href(soup_objects):
    result = {'title':[], 'link':[]}

    for soup in soup_objects:

        news_section = soup.select('div[id=main_pack] > div.news.mynews.section._prs_nws > ul.type01 > li')
        
        for news in news_section:
            a_tag = news.select_one('dl > dt > a')

            news_title = a_tag['title'] # title
            news_link = a_tag['href']   # link

            result['title'].append(news_title)
            result['link'].append(news_link)
    
    return result




search_input = '광주인공지능사관학교'

soups = get_news_soup_objects(search_input)
result_news = get_title_and_href(soups)

for title, link in zip(result_news['title'], result_news['link']):
    print(title, link, '\n')


# Write csv file
with open('./data/naver_news1.csv', 'w', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, lineterminator = '\n' )
    writer.writerow(result_news.keys())
    writer.writerows(zip(*result_news.values()))







