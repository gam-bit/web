# * 네이버 스마트 스토어 스크래핑 *
import requests
from bs4 import BeautifulSoup
import json
import csv



headers = {
    'authority': 'search.shopping.naver.com',
    'accept': 'application/json, text/plain, */*',
    'urlprefix': '/api',
    'logic': 'PART',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EC%9A%B4%EB%8F%99%ED%99%94&pagingIndex=3&pagingSize=40&productSet=total&query=%EC%9A%B4%EB%8F%99%ED%99%94&sort=rel&timestamp=&viewType=list',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NNB=I4CUENPXYEBV6; ASID=dc5f2a1100000173325716940000005b; MM_NEW=1; NFS=2; MM_NOW_COACH=1; _fbp=fb.1.1594904483661.1927880903; _ga=GA1.1.409323617.1594904484; _ga_4BKHBFKFK0=GS1.1.1594904483.1.1.1594904514.29; NRTK=ag#30s_gr#2_ma#-2_si#-2_en#-2_sp#-2; nx_ssl=2; BMR=s=1597024332905&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.nhn%3FblogId%3Dsuwon_man91%26logNo%3D221383387498%26proxyReferer%3Dhttps%3A%252F%252Fwww.google.com%252F&r2=https%3A%2F%2Fwww.google.com%2F; AD_SHP_BID=30; JSESSIONID=0657C5F808A6392847B6941C954C9D6F; page_uid=UzvEmsp0JXVss4LCfhNsssssszC-515981; spage_uid=UzvEmsp0JXVss4LCfhNsssssszC-515981',
}



params = (
    ('sort', 'rel'),
    ('pagingIndex', '2'),
    ('pagingSize', '80'),
    ('viewType', 'list'),
    ('productSet', 'total'),
    ('frm', 'NVSHATC'),
    ('query', '운동화'),
    ('origQuery', '운동화'),
    ('iq', ''),
    ('eq', ''),
    ('xq', ''),
)

response = requests.get('https://search.shopping.naver.com/search/all', headers=headers, params=params)
shopping_data = response.json()
product_data = shopping_data['productResult']['products']


# print(shopping_data)
# print(type(shopping_data)) # dict

# print(product_data[0])
# print(type(product_data)) # list of dict
print(len(product_data))


key_list = []
for product in product_data:
    key_list += list(product.keys())
key_list = list(set(key_list))



# params = (
#     ('sort', 'rel'),
#     ('pagingIndex', '3'),
#     ('pagingSize', '50'),
#     ('viewType', 'list'),
#     ('productSet', 'total'),
#     ('frm', 'NVSHATC'),
#     ('query', '운동화'),
#     ('origQuery', '운동화'),
#     ('iq', ''),
#     ('eq', ''),
#     ('xq', ''),
# )

# response = requests.get('https://search.shopping.naver.com/search/all', headers=headers, params=params)
# shopping_data = response.json()
# product_data = shopping_data['productResult']['products']




# with open('./data/naver_shopping.csv', 'w') as csvfile:
#     fieldnames = key_list
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames, restval=None, lineterminator = '\n')
#     writer.writeheader()
#     writer.writerows(product_data)


