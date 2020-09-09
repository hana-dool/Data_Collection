import time
from selenium import webdriver


# 1. 네이버 이동
browser = webdriver.Chrome()
browser.get('http://naver.com')

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name('link_login')
elem.click()

# 3. id / pw 입력
# id 가 써져있는 공간을 찾고, 거기에 send key 를 통해 아이디 입력
browser.find_element_by_id('id').send_keys('naver_id')
browser.find_element_by_id('pw').send_keys('password')

# 4. 로그인 버튼 클릭
browser.find_element_by_id('log.login').click()

# 그냥 하게되면, 홈페이지의 딜레이 떄문에 다음, 새로운 아이디 입력하는것이 되지 않는다.
time.sleep(3) # 3초 기달렸다가 다시하기

# 5. 다시 로그인 시도
# clear : 그 전에 로그인이 실패했던 아이디를 계속 남기는 탓에 뒤에 naver_id1 뒤에 새로운 아이디가 붙어나온다.
# 그래서 우리는 naver_id2 를 먼저 전의 정보를 지우고 시도해야한다.
browser.find_element_by_id('id').clear()
browser.find_element_by_id('id').send_keys('naver_id2')

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
# browser.close() # 현재탭만종료
browser.quit()