import os

os.chdir('/var/jenkins_home/workspace/test_01/test_pytest')
print(os.getcwd())
os.system('python -m pytest --alluredir ./report/allure_raw --clean-alluredir')
print('pytest start')
os.system('python -m allure serve report/allure_raw')
print('allure start')
