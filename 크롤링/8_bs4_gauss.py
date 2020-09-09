import requests
from bs4 import BeautifulSoup

# 가우스 전자 해당되는 url 복사
url = 'https://comic.naver.com/webtoon/list.nhn?titleId=675554'

# class 가 제목인거 같다.
# 테그 이름이 a 이고 , class 가 title 인 모든것을 가져와보자
res = requests.get(url)
res.raise_for_status

soup = BeautifulSoup(res.text,'lxml')


#------------- 만화제목 + 링크 가져오기 -----------------#
cartoons = soup.find_all('td', attrs={'class':'title'})
title = cartoons[1].a.get_text()
print(title) 
# 오 잘 가져오고 있음을 알 수 있다.
# 제목과 링크를 이어지도록 하고싶다.
link = cartoons[0].a['href']
print(link) # 아니 링크가 이상하다. 앞의 http ~ com 까지의 정보가 없다.
print('https://comic.naver.com' + link) # 그래서 앞에

# 나오는 화면에 대해서 모두 가져오고싶다고 하자.
for cartoon in cartoons :
    title = cartoon.a.get_text()
    link = 'https://comic.naver.com' + cartoon.a['href']
    print(title,link)


#---------------- 평점 구하기 ---------------------#
total_rate = 0
cartoons = soup.find_all('div', attrs={'class':'rating_type'})
for cartoon in cartoons:
    rate = cartoon.find('strong').get_text()
    print(rate)
    total_rate +=float(rate) # 기본적으로 출력은 str 이라서
print('전체 점수 :', total_rate)
print('평균 점수 :', total_rate/len(cartoons))