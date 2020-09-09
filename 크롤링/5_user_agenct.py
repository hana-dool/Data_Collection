# pc / 모바일에서 페이지를 접속했을떄 각기 다른 값이 나온다. 
# 만약 컴퓨터가 접속했을 떄 , 접속을 차단할 수 있다.(서버는 얘가 핸드폰?컴퓨터? 인지 과부하걸림 그래서 차단)

# 앞 3.request 에서는 그냥 하면 사이트에서 접근을 막는다. 
# 그래서 403 에러가 날 떄가 있다 
# 이럴때에는 아래와 같이 get 을 할 떄에 hearders 를 지정해서 해야한다.
import requests
url = 'http://nadocoding.tistory.com'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
# 이렇게 user agent 를 지정해주면 잘 읽어오게 된다.

res = requests.get(url,headers=headers)
print('응답코드: ', res.status_code)

res.raise_for_status()

# 파일로 만들기 
# 받은 text 를 저장한다.
with open('nadocoding.html','w',encoding = 'utf8') as f:
    f.write(res.text)
