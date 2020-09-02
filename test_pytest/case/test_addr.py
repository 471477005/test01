import os
import allure
import pytest
from test_pytest.pages.addr_page import addr
from test_pytest.common.read_yml import readyml

'''
allure 使用方法
https://www.cnblogs.com/123blog/p/12499802.html
'''

#==============相对路径找文件=================
curpath=os.path.dirname(os.path.realpath(__file__))
a=readyml(os.path.join(curpath,'testdata.yml'))
testdata = a['test_addr']
print(testdata)



@pytest.mark.parametrize(('name','phone','alladdr'),testdata)
@allure.feature('模块名称：添加地址模块')
@allure.story('用户故事：测试2.0版本添加地址功能')
@allure.title('用例标题：测试姓名、手机号越界前端是否有明确提示')
class Testaddr():
    # @allure.title("添加食材-进入购物车-结算成功")
    @allure.testcase("http://192.168.2.50:8080/browse/AID-621")
    def test_addr(self,login,name,phone,alladdr):
        driver=login
        web = addr(driver)
        web.driver.get('http://staging.lsspgyl.com/purchaser/#/center/account/address')
        web.go_addr_page()
        web.input_name(name)
        web.input_phone(phone)
        web.input_city()
        web.input_all_addr(alladdr)
        web.save()

if __name__ == '__main__':
    pytest.main()
    # os.system('d: && cd D:\启明星\demo_pytest && pytest --alluredir ./report/allure_raw')
    # os.system('allure serve report/allure_raw')
