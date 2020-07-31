#-*- coding: UTF-8 -*- 
import allure
import pytest

from test_pytest.common.basepage import BasePage

host = "http://staging.lsspgyl.com"
login_url = host + "/purchaser/#/login"

class LoginPage(BasePage):
    '''登录页面'''

    loc_账号 = ("xpath", '//*[@id="app"]/div[1]/div/div/div/form/div[1]/div/div/div/input')
    loc_密码 = ("xpath", '//*[@id="app"]/div[1]/div/div/div/form/div[2]/div/div/div/input')
    loc_登陆 = ('xpath', '//*[@id="app"]/div[1]/div/div/div/form/button/span')

    #鼠标悬浮
    loc_悬浮 = ('xpath','//*[@id="app"]/div[1]/div/div[2]/span[3]/span')

    # 判断页面元素
    loc4 = ("xpath", '//*[@id="app"]/div[4]/div/div[1]/div[2]/div[1]/span')

    @allure.step("登录步骤：输入账号")
    def input_user(self, username):
        '''输入账号'''
        self.clear_text(self.loc_账号,'清除账号内容')
        self.input_text(username,self.loc_账号,'输入账号')

    @allure.step("登录步骤：输入密码")
    def input_psw(self, psw):
        '''输入密码'''
        self.clear_text(self.loc_密码, '清除密码内容')
        self.input_text(psw, self.loc_密码, '输入密码')

    @allure.step("登录步骤：点登陆按钮")
    def click(self):
        self.click_button(self.loc_登陆,"点击登陆按钮")

    @allure.step("登录")
    def test_login(self, username="13000000000", psw="qwe123456"):
        self.driver.get(login_url)
        self.input_user(username)
        self.input_psw(psw)
        self.click()

    @allure.step("判断是否登录成功, 返回bool值")
    def is_login_success(self):
        '''悬浮后判断是否登录成功, 返回bool值'''
        self.suspend_mouse(self.loc_悬浮,'悬浮查看用户姓名元素')
        text = self.get_elements_text(self.loc4,'获取采购额公示')
        print("登录完成后，获取页面文本元素:%s"%text)
        return ['采购额公示'] ==  text


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    web = LoginPage(driver)
    driver.get(login_url)
    web.test_login()

    # 判断登录
    result = web.is_login_success()
    print(result)
    driver.quit()
    assert result
    # pytest.main()


