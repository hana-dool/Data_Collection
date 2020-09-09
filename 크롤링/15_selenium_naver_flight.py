from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = 'https://flight.naver.com/flights/'
browser.get(url) # url 로 이동

# 가는날 선택 이라는 text 로부터 element를  추출하자.
browser.find_element_by_link_text('가는날 선택').click()
# 이번달 27 ~ 다음달 3  선택

# 27이라는 글자를 가지는 모든 element 중에서 첫번쨰(이번달) 
browser.find_elements_by_link_text('27')[0].click()
# 3이라는 글자를 가지는 모든 element 중에서 두번째 (다음달) 의 정보
browser.find_elements_by_link_text('3')[1].click()


# 제주도 선택
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]').click()

# 항공권 검색 클릭
browser.find_element_by_xpath('//*[@id="searchArea"]/a').click()

# 아래 방식이 안될떄가 있다. 이는 로딩시간떄문
# 이런 동작이 많을 경우, 로딩이 언제 끝나는지 알 수 없다.
# 앞의 경우처럼 time 을 줘도 별로 안좋다.
# 이런식으로 할 수 있따. 10초를 기다리되, 엘레멘트가 뜨면 그떄 크롤링시도

# 10초 기다리되 (10 초넘으면 에러) , 10초안에 조건(EC) 에서 , X_PATH 의 조건으로, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]' 에 해당하는 엘레멘트가 나올떄까지
try: # 성공했을떄의 동작
    elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
    print(elem.text)
finally: # 실패하거나/ 끝날떄 quit 으로 브라우저 종료
    browser.quit()
# 첫번째 결과 출력
# elem = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')
# elem.text