import requests
import csv
from bs4 import BeautifulSoup

# 저장할 csv 객체 만들기
filename = 'rating.csv'
f = open(filename,'w',encoding='utf8',newline='')
writer = csv.writer(f)

# colnames 형성하기
title = ['체널','프로그램','시청자수']
writer.writerow(title)

# url 불러오기
url = 'https://www.nielsenkorea.co.kr/tv_terrestrial_day.asp?menu=Tit_1&sub_menu=1_1&area=00&begin_date=20200603'
res = requests.get(url)
res.raise_for_status()

# soup 객체 만들기
soup = BeautifulSoup(res.text,'lxml')

# html 로 만들어서 과연 위 url 로 충분하게 나오는지 점검
with open('check.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())
    
# 옆에서 저장된 html 에서 내가 원하는 정보가 있음을 확인하고, 크롤링을 시작하자
# 크롬에서 본 결과, 데이터는 table -> tbody 안에 여러 tr들로 구분되어 data 가 구분되어있다.
# tr 하나하나는 sample data 를 의미하고, 하나의 tr 안에는 td 형태로 feature 들로 구성되어있다.
# 즉 table 찾기 -> 그 안에서 tbody 찾기 -> 그 안에서 '모든' tr 찾기  의 과정으로 데이터를 모두 뽑아내자.

# tr 로 접근
data_rows =soup.find_all('table',attrs={'class':'ranking_tb'})
ratings = data_rows[0]

# sample 만 추려내기
data_rosws = ratings.find_all('tr')

for idx, row in enumerate(data_rows):
    # 하나하나의 tr(sample) 에는 td(feature) 데이터들이 숨어있다. 이것을 모두 뽑아내자.
    columns = row.find_all('td')
    data = [col.get_text() for col in columns]
    print(data)
    writer.writerow(data)
