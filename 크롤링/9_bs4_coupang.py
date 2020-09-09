# 노트북을 사야한다.
# 리뷰가 많고, 평점이 높은것을 고르고, 광고가 아닌것, 당일배송을 골라내고싶다.
# 주소를 이용해서 (page) scraping 을 할 수 있을거같다!

# [ http method 에는 몇가지가 있다. get, post 방식]
# get, post 방식이 있다.

# get : 어떤 내용을 누구나 볼 수 있게 url 을 적어서 보냄
# httpL//www,coupang.com/np/serach?minPrice=1000&maxPrice=100000&page=1
# 물음표가 나오고 뒤에 정보가 나온다.
# get은 ? 뒤의 변수와 값들, 여러개가 붙을 수 있다. 이 떄는 위의 값들을 변경하면서 쉽게 변경 가능 
# 각 정보들은 & 로 나누어져있다. 
# 한번 전송할 때 정보량이 제한이 있어 큰 값을 보낼 수 없다.

# post : html 의 body 에 숨긴 데이터
# 보안데이터는 post 형식으로 숨겨보낼 수 있다.
# 크기에 제한이 없어서 복잡하고 큰 데이터를 보낼 수 있다.

import requests
import re
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

for pg in range(1,5):
    url = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={0}&rocketAll=false&searchIndexingToken=1=4&backgroundColor='.format(pg)
    # 이거 headers 없이하면 에러난다.
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,'lxml')
    #잘 읽어오나 확인 print(res.text)

    items = soup.find_all('li',attrs={'class':re.compile('^search-product')})
    # re.compile : search-product 로 시작하는 모든것을 다 데리고온다.
    # print(items[0].find('div',attrs={'class':'name'}).get_text())
    # 위 처럼 하면 이름 정보를 뽑아오게 된다.

    # 최근의 많은 데이터들에 대해서, 에플 제외 / 평점 4.5 이상 / 평점 수 100개 이상 / 광고 제외 인 경우만 보고싶을떄

    for item in items:
        name = item.find('div',attrs={'class':'name'}).get_text() 
        # 애플상품 제외
        if 'Apple' in name:
            print('애플상품 제외')
            continue
        price = item.find('strong',attrs={'class':'price-value'}).get_text()
        rate = item.find('em',attrs={'class' : 'rating'})
        # 아래 과정은 rate(평점) 의 경우 비어있을 수 있어서 (그러면 none 이 나온다.) 비어있는 경우 아예 넣지 않도록 하는 작업이 필요하기 떄문
        if rate :
            rate = rate.get_text()
        else:
            rate = '평점없음'
            print('평점없는상품 제외')
            continue
        ad = item.find('span',attrs={'class' : 'ad-badge-text'})
        # 이 과정은 ad 가 있는경우 , 다시 되돌아가는 문구이다. 
        if ad : 
            print('광고상품 제외')
            continue
        rate_cnt = item.find('span', attrs={'class':'rating-total-count'})
        # 아래 과정은 평점 수가 비어있을 때 오류 방지를 위한 열
        if rate_cnt :
            rate_cnt = rate_cnt.get_text()
            rate_cnt = rate_cnt[1:-1] # count 의 경우는 (14) 이런식으로 나오기 떄문에
        else :
            rate_cnt = '평점없음'
            print('평점수없는 상품 제외')
            continue
        # 나는 평점이 4.5 이상 / 리뷰 수는 50개 이상인 경우만 보고싶다.
        link = item.find('a',attrs={'class':'search-product-link'})['href']
        # link 를 넣고싶은 경우
        if float(rate) >= 4.5 and float(rate_cnt)>=100:
            print(f'제품명 : {name}')
            print(f'가격 : {price}')
            print(f'평점 : {rate}점 {rate_cnt}개')
            print('링크 {}'.format('https://www.coupang.com/'+link))
            print('-'*30) # 줄긋기

link = item.find('a',attrs={'class':'href'})

