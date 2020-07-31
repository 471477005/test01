import os

os.chdir('/var/jenkins_home/workspace/test_01/test_pytest')
print(os.getcwd())
os.system('pytest --alluredir ./report/allure_raw --clean-alluredir')
os.system('allure serve report/allure_raw')

