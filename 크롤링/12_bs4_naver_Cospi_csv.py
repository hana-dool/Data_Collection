import requests
import csv
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page='

filename = '시가총액 1-200.csv'
f = open(filename,'w',encoding='utf8',newline='')
# 엑셀파일 열때 한글파일이름이 꺠지면 encoding 을 utf-8-sig 로 바꾸다.
# csv 모듈에서 데이타를 쓸 때 각 라인 뒤에 빈 라인이 추가되는 문제가 있는데, 이를 없애기 위해 (파이썬 3 에서) 파일을 open 할 때 newline='' 와 같은 옵션을 지정한다
# 공백을 넣지 않으면 , 한줄 넣고 띄어져 버린다...
writer = csv.writer(f)
#CSV 파일을 쓰기 위해서는 .csv 파일을 쓰기모드로 오픈하고 파일객체를 csv.writer(파일객체) 에 넣으면 된다. 
# CSV writer는 writerow() 라는 메서드를 통해 list 데이타를 한 라인 추가하게 된다.

title = 'N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE'.split('\t')
writer.writerow(title)

for page in range(1,5):
    res = requests.get(url+str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text,'lxml')

    data_rows = soup.find('table',attrs={'class' : 'type_2'}).find('tbody').find_all('tr')
    for row in data_rows :
        columns = row.find_all('td')
        if len(columns) <= 1: # 의미없는 데이터는 스킵
            continue
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)

