from selenium import webdriver

browser = webdriver.Chrome('./chromedriver.exe')
# 현재 내 폴더의 경로에 있으므로 ./ 으로 경로설정
browser.get('http://www.naver.com')
elem = browser.find_element_by_class_name('link_login')
elem.click()

browser.back()    # 뒤로
browser.refresh() # 새로고침
browser.forward() # 앞으로
browser.back()

elem = browser.find_element_by_id('query')
from selenium.webdriver.common.keys import Keys
elem.send_keys('나도코딩')
elem.send_keys(Keys.ENTER)

# a 라는 테그에 해당되는 값을 불러온다.
# 제일 먼저 만난것을 불러옴
elem = browser.find_element_by_tag_name('a')
elem

# a 라는 태그에 해당되는 모든 값을 가져온다.
elem = browser.find_elements_by_tag_name('a')
elem

for e in elem:
    e.get_attribute('href')# href 에 해당하는 elemt 를 모두 불러온다.

# ---- 다음! ----- # 
browser.get('http://daum.net')
# 검색창에서 NAME 속성이 q 임을 이용해 검색창을 찾을 수 있다.
elem = browser.find_element_by_name('q')
# 검색창에 '검색' 입력
elem.send_keys('검색')
# 검색창에서 enter 쳐서 검색
elem.send_keys(Keys.ENTER) # 엔터를 칠 수 있다.

elem = browser.find_element_by_name('q')
elem.send_keys('검색2')

# 이때에 주의해야할 것은 아래 '' 안에 "" 이므로 , 밖에는 "" 으로 처리하면 겹쳐서 안된다 
elem = browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]')
# 클릭 동작! 
elem.click()

# 현재 탭만 닫기
browser.close()

# 모든 브라우저 닫기
browser.quit()
