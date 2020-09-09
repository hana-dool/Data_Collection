
from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

url = 'https://play.google.com/store/movies/top'
browser.get(url)

# 이제 스크롤을 밑으로 내려야 한다.
# 이 동적 행동을 하기 위해서는 java script code 를 사용해야한다.
# selenium 에서는 java 를 쓸 수 있음

# 모니터 해상도 높이인 1080 만큰 스크롤 내리기
# 하지만 이 경우는 맨 아래까지 내려가지 못하고있다.
# browser.execute_script('window.scrollTo(0,1080)') # 1080 은 우리 pc 의 세로 높이

# 하지만 우리가 해야하는것은 화면 가장 아래로 스크롤을 내려야 한다.
# 근데 로딩 속도떄문에 로딩되기 전에 내려가서 잘 내려가지 못하고 있다.
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

prev_height = browser.execute_script('return document.body.scrollHeight')
import time
# 반복수행
interval = 2
while True:
    # 스크롤 아래로 내리기
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    # 대기
    time.sleep(interval)
    # 업데이트 된 현재높이를 저장
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if curr_height == prev_height:
        # 현재 / 과거 높이가 같으면 당연히 끝
        break
    prev_height = curr_height
print('스크롤 완료')

#------- 크롤링을 위한 코드 --------#

import requests
from bs4 import BeautifulSoup

# 위에서 seleium 에서 얻은 페이지 정보에 대해 page source를 가져온다.
# 스크롤을 모두 내렸을떄의 정보일 것이다.
soup = BeautifulSoup(browser.page_source,'lxml')
movies = soup.find_all('div',attrs={ 'class' : 'ImZGtf mpg5gc'})
print(movies) 

with open('movie.html','w',encoding='utf8') as f :
    f.write(soup.prettify()) # html 을 예쁘게 나오게 한다. soup.prettify 는 말그대로 pretty ! 

# 하지만 이런식으로 하게되면 초기 10개밖에 보이지 않다. 
# 동적으로(마우스 스크롤을 내려야) 더 많은 정보를 얻는데, 이 떄에 우리는 그저 처음 뜨는 10개 정보만 받은것.. 


for movie in movies :
    title = movie.find('div',attrs = {'class' : "WsMG1c nnK0zc"}).get_text()
    print(title)