from selenium import webdriver
options = webdriver.ChromeOptions()
options.headless = True # 백그라운드에서 크롬이 들어간다.
options.add_argument('window-size=1920x1080')
# 여기서 user agent 를 먼저 지정해주면 아래에서 headliss 가 아니라 chrome 으로 잘 적용된다.
# headless 를 쓰게된다면 이처럼 user-agent 를 바꾸어주는것이 중요하다. 
options.add_argument('user-agent=User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36')

browser = webdriver.Chrome(options=options) 
browser.maximize_window()

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'
browser.get(url)

id_ = browser.find_element_by_id('detected_value')
print(id_.text) 
# headless 가 chrom 으로 뜬다. 
# headless 를 쓰게되면, 자체 사이트에서 막을 수 있다.
# ㅇUser
browser.quit()
