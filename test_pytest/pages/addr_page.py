from test_pytest.common.basepage import BasePage
import allure



class addr(BasePage):
    '''测试添加地址页面'''
    loc_返回首页=('xpath','//*[@id="search-bar"]/div/img')
    loc_悬浮头像=("xpath",'//*[@id="app"]/div[1]/div/div[2]/span[3]/span')
    loc_点击地址=('xpath','//*[@id="el-popover-1980"]/div[1]/div[2]/div[3]')
    loc_点击添加地址=('xpath','//*[@id="app"]/div[4]/div/div/div/div/div/div/div[1]/div[2]/div[2]/div/h1/div')
    loc_姓名=('xpath','//*[@id="app"]/div[4]/div/div/div/div/div/div/div[3]/div/div[2]/form/div[1]/div/div[1]/input')
    loc_手机号 = ('xpath', '//*[@id="app"]/div[4]/div/div/div/div/div/div/div[3]/div/div[2]/form/div[2]/div/div[1]/input')
    loc_城市 = ('xpath', '//*[@id="app"]/div[4]/div/div/div/div/div/div/div[3]/div/div[2]/form/div[3]/div/div/div[1]/input')
    loc_北京市 = ('xpath', '//span[text()="北京市"]')
    loc_直辖区 = ('xpath', '//span[text()="直辖区"]')
    loc_详细地址 = ('xpath', '//*[@id="app"]/div[4]/div/div/div/div/div/div/div[3]/div/div[2]/form/div[4]/div/div[1]/textarea')
    loc_保存 = ('xpath', '//*[@id="app"]/div[4]/div/div/div/div/div/div/div[3]/div/div[3]/div/button[2]/span')
    @allure.step("进入新增地址页面")
    def go_addr_page(self):
        '''首页进入到新增地址页面'''
        # self.click_button(self.loc_返回首页,'返回采购方首页')
        # self.suspend_mouse(self.loc_悬浮头像, '悬浮个人头像按钮')
        # self.click_button(self.loc_点击地址,'点击地址按钮')
        self.click_button(self.loc_点击添加地址,'点击添加地址按钮')


    @allure.step("输入姓名")
    def input_name(self,name):
        '''输入姓名'''
        self.clear_text(self.loc_姓名, '清除姓名输入框内容')
        self.input_text(name,self.loc_姓名,'输入姓名输入框')

    @allure.step("输入手机号")
    def input_phone(self,phone):
        '''输入手机号码'''
        self.clear_text(self.loc_手机号, '清除手机号输入框内容')
        self.input_text(phone, self.loc_手机号, '输入手机号输入框')

    @allure.step("选择城市")
    def input_city(self):
        '''选择城市'''
        self.click_button(self.loc_城市, '点击城市')
        self.click_button(self.loc_北京市,'点击北京市按钮')
        self.click_button(self.loc_直辖区,'输入直辖区')

    @allure.step("详细地址")
    def input_all_addr(self,all_addr):
        '''输入详细地址'''
        self.clear_text(self.loc_详细地址, '清除详细地址内容')
        self.input_text(all_addr, self.loc_详细地址, '输入详细地址')

    def save(self):
        '''保存'''
        self.click_button(self.loc_保存, '点击保存按钮')

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
        web = addr(driver)
        web.driver.get('http://staging.lsspgyl.com/purchaser/#/center/account/address')
        web.go_addr_page()
        web.input_name('xingming')
        web.input_phone('13000000000')
        web.input_city()
        web.input_all_addr('详细地址')
        web.save()
