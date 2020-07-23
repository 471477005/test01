import yaml


def readyml(filePath):

    f = open(filePath, "r", encoding="utf-8")
    y = f.read()
    data = yaml.load(y, Loader=yaml.FullLoader)
    print("读取yaml转字典:%s"%data)
    return data

if __name__ == '__main__':
    a = readyml(r'D:\启明星\demo_pytest\case\testdata.yml')
    print(a['test_addr'])