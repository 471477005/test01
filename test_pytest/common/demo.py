import time
from datetime import datetime

from selenium import webdriver

from test_pytest.common.constants import OUTPUTS_DIR

class scr:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')

    def save_screenshot(self,img_doc):
        '''
        页面截屏保存截图
        :param img_doc: 截图说明
        :return:
        '''
        file_name = OUTPUTS_DIR + "\\{}_{}.png".format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"), img_doc)
        # file_name = 'abc.png'
        time.sleep(1)
        print(file_name)
        self.driver.save_screenshot(file_name)
        print('123456789')
scr().save_screenshot('nihao')