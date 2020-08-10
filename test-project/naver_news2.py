# -*- encoding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv


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



search_input = '광주인공지능사관학교'
soups = get_news_soup_objects(search_input)




for soup in soups:

    news_section = soup.select('div[id=main_pack] > div.news.mynews.section._prs_nws > ul.type01 > li')
    print(news_section)
    # for news in news_section:
    #     a_tag = news.select_one('dl > dt > a')

    #     news_title = a_tag['title'] # title
    #     news_link = a_tag['href']   # href
        
    #     my_dict = {
    #         'title': news_title,
    #         'link': news_link
    #     }

    #     # Write csv file    
    #     with open("./data/naver_news2.csv", 'a', encoding='utf-8') as csvfile:
    #         fieldnames = ['title', 'link']
    #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')
    #         # writer.writeheader()
    #         writer.writerow(my_dict)
















