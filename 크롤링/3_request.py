import requests
res = requests.get('http://naver.com')
#res = requests.get('http://nadocoding.tistory.com')
print('응답코드: ', res.status_code)
 # 200 이면 잘 받아온것이다. 
 # 403 이면 받아올 권한이 없는것이다.

res.raise_for_status()
# 이 경우 문제가 생기면 바로 에러를 출력한다.

print(len(res.text)) # 텍스트 길이를 출력
print(res.text)

# 파일로 만들기 
# 받은 text 를 저장한다.
with open('mygoogle.html','w',encoding = 'utf8') as f:
    f.write(res.text)

