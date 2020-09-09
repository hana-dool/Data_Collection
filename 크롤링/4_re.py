# 정규식은 매우 많다. 
# 필요한 부분 (자주 쓰이는 부분을 정리하자)

import re
# 4자리의 문자를 가져오고싶다고 하자.
# ca?e
# care case cave .... 가 가능할 것이다.
# 이런것들을 모두 검색하려 할 때 어떻게 할 수 있을까 ? 


p = re.compile("ca.e") 
# 어떤 정규식을 컴파일할지
# 문자열의 시작, 끝을 나타내는 컴파일을 형성 가능하다. 
# . (ca.e): 하나의 문자를 의미한다. -> care / cafe / case .. 가능  대산 caffe 불가능
# ^ (^de): 문자열의 시작을 의미한다 -> desk/ destination ... 가능 대신 fade 불가능
# $ (se$) : 문자열의 끝을 의미한다. -> case / base ... 가능 대신 face 는 불가능 

m = p.match('case') 
print(m.group())
# 정규식이 위의 조건과 같으면 에러가 발생되지 않다. 
# 매칭되지 않으면 에러가 발생한다. 

m = p.match('fase')
print(m.group())

# 함수를 만들어서 match 가 되면, 주어진 것을 프린트하고. 그렇지 않으면 에러를 만드는 함수를 정의
def print_match(m):
    if m : 
        print('m.group() :',m.group()) # 일치하는 문자열 반환
        print('m.string :',m.string) # 입력받은 문자열 (string 은 변수라서 ()없음)
        print('m.start() :',m.start()) # 일치하는 문자열의 시작 index
        print('m.end() :',m.end()) # 일치하는 문자열의 끝 index
        print('m.span() :',m.span()) # 일치하는 문자역의 시작,끝 index
    else : 
        print('매칭되지 않음')

m = p.match('careless') 
# match : 주어진 문자열의 처음부터 일치하는지 확인
# 이 경우에는 care 을 print 한다. 
# 처음부터 쭉 이어나가면 care 이 매칭이 되었으므로, 그 뒤는 더 고려하지 않는다.
print_match(m) 

m = p.search('good care')
# search : 주어진 문자열 중에 일치하는게 있는지 확인
print_match(m) 
# care 를 잘 출력하는것을 볼 수 있다.

lst1 = p.findall('careless')
lst2 = p.findall('good care cafe')
# findall : 일피하는 모든것을 리스트 형태로 반환
print(lst1)
print(lst2) # 일치하는 2개를 모두 쓴다.

#---------순서------------#
# 1. p = re.compile('원하는 형태')
# . (ca.e): 하나의 문자를 의미한다. -> care / cafe / case .. 가능  대산 caffe 불가능
# ^ (^de): 문자열의 시작을 의미한다 -> desk/ destination ... 가능 대신 fade 불가능
# $ (se$) : 문자열의 끝을 의미한다. -> case / base ... 가능 대신 face 는 불가능 
# 2. m = p.match('비교할 문자열') : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search('비교할 문자열') : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall('비교할 문자열) : 일치하는 모늗것을 리스트 형태로 변환

