import os

# 获取项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取Configs目录路径
CONFIG_DIR = os.path.join(BASE_DIR, 'Configs')

# 获取配置文件路径
CONFIG_FILE_PATH = os.path.join(CONFIG_DIR, 'init.ini')

# 获取TestDatas目录路径
DATAS_DIR = os.path.join(BASE_DIR, 'TestDatas')

# 获取excel文件路径
DATAS_FILE_PATH = os.path.join(DATAS_DIR, 'TestDatas.xlsx')

# 获取Logs目录路径
LOGS_DIR = os.path.join(BASE_DIR, 'Logs')

# 获取Reports目录路径
REPORTS_DIR = os.path.join(BASE_DIR, 'Reports')

# 获取TestCases目录路径
CASES_DIR = os.path.join(BASE_DIR, 'TestCases')

#获取
OUTPUTS_DIR = os.path.join(BASE_DIR, 'screenshot')

# print(BASE_DIR)
# print(CONFIG_DIR)
# print(CONFIG_FILE_PATH)
# print(OUTPUTS_DIR)