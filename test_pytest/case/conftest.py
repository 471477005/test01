from selenium import webdriver
import time
import pytest
from test_pytest.pages.login_page import LoginPage
import platform

@pytest.fixture(scope="session")
def driver(request):
    '''定义全局driver'''
    sys = platform.system()
    if sys == "Windows":
        _driver = webdriver.Chrome()
        _driver.maximize_window()  # 最大化
        print(_driver.title)

    elif sys == "Linux":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument('--start-maximized') # 最大化运行（全屏窗口）设置元素定位比较准确
        chrome_options.add_argument("--window-size=1920,1080")  # 专门应对无头浏览器中不能最大化屏幕的方案
        _driver = webdriver.Chrome(options=chrome_options)
        _driver.maximize_window()  # 最大化
        print(_driver.title)

    def end():
        '''测试用例完成后，执行终结函数'''
        time.sleep(5)
        _driver.quit()

    request.addfinalizer(end)
    return _driver



@pytest.fixture(scope="session")
def login(driver):
    '''前置：登录'''
    web = LoginPage(driver)
    web.test_login()

    result = web.is_login_success()
    print(result)
    assert result

    return driver
