from selenium import webdriver

option = webdriver.ChromeOptions()


option.add_argument('headless')

browser = webdriver.Chrome(options=option)
browser.get('http://www.baidu.com')
print(browser.title)
browser.quit()
