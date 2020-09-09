import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday.nhn'

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')
# 우리가 가져온 html 문서를 lxml의 해석기를 이용해 beautiful soup 객체로 형성

print(soup.title) 
# soup 객체를 통해서 element 에 바로 접근 가능

print(soup.title.get_text())
# 이렇게 하면 text 만 접근 가능

print(soup.a)
# soup 은 모든 html 을 가지고 있다.
# 첫번쨰 발견되는 a 테그의 정보를 출력해줘

print(soup.a.attrs)
# attributes 즉 각 속성을 알려준다.
# dict 형태로 나오게 된다.

print(soup.a['href']) 
# a element 의 href 속성 정보를 알려준다.

soup.find('a',attrs={'class':'Nbtn_upload'})
# 뒤에 나오는 거에 해당되는것의 첫 정보를 알려준다.
# 이 경우 a 테그에서 attributs (class) 가 Nbtn_upload 인 것을 찾아줘!

soup.find(attrs={'class':'Nbtn_upload'})
# 모든 태그에서 class 가 Nbtn_upload 인 것을 찾아줘

print(soup.find('li',attrs={'class':'rank01'}))
# li 탭에서 class 가 rank01 인 것의 정보를 알려주고있다.
# herf가 포함된 모든 정보들을 알려주고 있다.

rank1 = soup.find('li',attrs={'class':'rank01'})
print(rank1.a)
# 객체를 형성한 뒤에 객체들을 찾아볼 수 있다.

# soup 객체에서 자식 , 부모 로 자유롭게 이동 가능하다.
# rank1 을 가지고 형재 element 들로 넘어가 보자.
print(rank1.a.get_text())
#rank1 에서 aclass 의 text 를 뽑아냈다.

rank1.next_sibling
rank2 = rank1.next_sibling.next_sibling
# 아니 2번했더니 뽑아낸다?
# 이는 줄바꿈을 했다는것이다.
rank3 = rank1.next_sibling.next_sibling
# next(다음) 의 값으로 넘어간다.

rank2 = rank3.previous_sibling.previous_sibling
rank2.a.get_text() 
# 이러면 rank1 의 값이 나온다.(즉 전의 siblings 가 나온다.)

print(rank1.parent)
# 부모가 가지고있는 모든값이 나온다.
# 즉 rank1 의 부모를 표출


#------ find_next_sibling -------# 
# 나 다음의 형제를  찾아낸다. 
rank2 = rank1.find_next_sibling('li')
# rank1 테그 기준으로 형제들을 찾는데 li 인것만 찾는다.
rank2.a.get_text()
rank3 = rank2.find_next_sibling('li')
rank3.a.get_text()

#------ find_previous_sibling ------# 
#나 이전의 형제를 찾아낸다.
rank2 = rank3.find_previous_sibling('li')
rank2.a.get_text()

#------ find_next_siblings --------#
# 매번 할 떄마나 하나의 이전/ 이후를 찾기 귀찮을떄
rank1.find_next_siblings('li')
# 보면 나 이후의 모든 형제들을 뽑아내고 있다.

# ------------- text 를 통해서 class 찾아내기 ---------------# 
webtton = soup.find('a',text = '독립일기-24화 쓰레기 줄이기') 
# 모든 a 테그중에서 text 가 독립일기-2... 인것을 찾아줘
print(webtton) 
# 위 조건을 만족하는 a 테그를 찾아준다.

# a 테그에서 시작되어서 a 다음은 띄어쓰기이다.
# oneclick , href, title 이 dict 처럼 정의되고 있음
# text 는 여는테그<> 와 닫는 테그 </a> 사이의 '독립일기-24화 쓰레기 줄이기' 이다.

#<a onclick="nclk_v2(event,'rnk*p.cont','748105','2')" 
#href="/webtoon/detail.nhn?titleId=748105&amp;no=25" 
#title="독립일기-24화 쓰레기 줄이기">독립일기-24화 쓰레기 줄이기</a>
