from test_pytest.common.basepage import BasePage
import allure

class testshoppingPage(BasePage):
    '''购物车页面'''
    loc_返回首页=('xpath','//*[@id="search-bar"]/div/img')
    loc_加入购物车=("xpath",'//*[@id="hot"]/div/div[2]/div[2]/div[2]/div[2]/span[2]/i')
    loc_我的购物车=('xpath','//*[@id="search-bar"]/div/div[2]/div/span/div')
    loc_去结算=('xpath','//*[@id="app"]/div[4]/div/div[1]/div[5]/div[2]/div')
    loc_确认收货地址=('xpath','//*[@id="app"]/div[4]/div/div/div[1]/div[1]/div')
    @allure.step("加入购物车")
    def click_add(self):
        '''列表页面加入购物车'''
        self.click_button(self.loc_返回首页,'返回采购方首页')
        self.click_button(self.loc_加入购物车, '点击加入购物车')

    @allure.step("我的购物车")
    def click_shopping(self):
        '''进入我的购物车'''
        self.click_button(self.loc_我的购物车,'进入我的购物车页面')

    @allure.step("去结算")
    def click_buy(self):
        '''编辑文章分类'''
        self.click_button(self.loc_去结算,'点击去结算按钮')

    @allure.step("判断是否进入订单页面")
    def is_login_success(self,addr):
        '''判断是否进入订单页面'''
        text = self.get_elements_text(self.loc_确认收货地址, '查看是否有收货地址四个字')
        print(addr)
        assert addr == text

if __name__ == '__main__':
        from selenium import webdriver
        from demo_pytest.pages.login_page import LoginPage
        driver = webdriver.Chrome()
        driver.maximize_window() # 最大化
        web = LoginPage(driver)
        web.test_login()
        res = web.is_login_success()
        print("登录结果：%s"%res)

        #购物车下单啦
        web = testshoppingPage(driver)
        web.click_add()
        web.click_shopping()
        web.click_buy()
        web.is_login_success()
