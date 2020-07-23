import os

os.chdir('D:\启明星\demo_pytest')
print(os.getcwd())
os.system('pytest --alluredir ./report/allure_raw --clean-alluredir')
os.system('allure serve report/allure_raw')

