import requests
from bs4 import BeautifulSoup

# user agent 없이 하면 구글 미국의 영화정보가 나오게 된다.(우리의 창에서는 한국 영화들이 나옴에도 불구하고)
url = 'https://play.google.com/store/movies/top'

# 그래서 headers 를 지정해 주어야 (유저정보) 한국정보를 가져오게 된다.
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
'Accept-Language':'ko-KR,ko'} # 추가적으로 accept-language 를 지정해주어야한다.

res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,'lxml')

movies = soup.find_all('div',attrs={ 'class' : 'ImZGtf mpg5gc'})
print(movies) 

with open('movie.html','w',encoding='utf8') as f :
    f.write(soup.prettify()) # html 을 예쁘게 나오게 한다. soup.prettify 는 말그대로 pretty ! 

# 하지만 이런식으로 하게되면 초기 10개밖에 보이지 않다. 
# 동적으로(마우스 스크롤을 내려야) 더 많은 정보를 얻는데, 이 떄에 우리는 그저 처음 뜨는 10개 정보만 받은것.. 


for movie in movies :
    title = movie.find('div',attrs = {'class' : "WsMG1c nnK0zc"}).get_text()
    print(title)

