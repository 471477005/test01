import os
import allure
import pytest
from test_pytest.pages.shopping_page import testshoppingPage
from test_pytest.common.read_yml import readyml

'''
allure 使用方法
https://www.cnblogs.com/123blog/p/12499802.html
'''

curpath=os.path.dirname(os.path.realpath(__file__))
a=readyml(os.path.join(curpath,'testdata.yml'))     #用相对路径读取文件
# a=readyml(r'D:\启明星\demo_pytest\case\testdata.yml')
testdata=a['Testshopping']


@pytest.mark.parametrize('addr',testdata)
@allure.feature("添加食材")
class Testshopping():
    @allure.title("添加食材-进入购物车-结算成功")
    @allure.testcase("http://192.168.2.50:8080/browse/AID-621")
    def test_add_shopping(self,login,addr):
        driver=login
        web = testshoppingPage(driver)
        web.click_add()
        web.click_shopping()
        web.click_buy()
        web.is_login_success(addr)

if __name__ == '__main__':
    pytest.main()
    # os.system('d: && cd D:\启明星\demo_pytest && pytest --alluredir ./report/allure_raw')
    # os.system('allure serve report/allure_raw')

