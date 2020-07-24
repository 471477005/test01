from selenium import webdriver
import time
import pytest
from test_pytest.pages.login_page import LoginPage

@pytest.fixture(scope="session")
def driver(request):
    '''定义全局driver'''
    _driver = webdriver.Chrome()
    _driver.maximize_window()  # 最大化

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


