import requests
from bs4 import BeautifulSoup

# 네이버 웹툰에 해당되는 url 복사
url = 'https://comic.naver.com/webtoon/weekday.nhn'


# class 가 제목인거 같다.
# 테그 이름이 a 이고 , class 가 title 인 모든것을 가져와보자
res = requests.get(url)
res.raise_for_status

soup = BeautifulSoup(res.text,'lxml')
cartoons = soup.find_all('a',attrs={'class':'title'})
# 테그 이름이 a 이고
# class 속성이 title 인 모든 정보를가져올 것이다
for cartoon in cartoons :
    print(cartoon.get_text())
# 이렇게 하면 모든 정보를 한번에 긁어온 것이다.
