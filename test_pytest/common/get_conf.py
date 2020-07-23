import logging,time,os
class HandleLogger:
    def __init__(self, path=None):
        # 文件命名
        if path is None:
            self.log_path = os.path.dirname(__file__)
        self.logname = os.path.join(self.log_path, '%s.log'%time.strftime("%Y-%m-%d"))      #日志地址
        # print(self.logname)
        self.logger = logging.getLogger()
        # print(self.logger)
        self.logger.setLevel(logging.DEBUG)     #设置日志级别    由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上

        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s[line:%(lineno)d] - fuc:%(funcName)s- %(levelname)s: %(message)s')  #这个类配置了日志的格式，在里面自定义设置日期和时间，输出日志的时候将会按照设置的格式显示内容。


    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname,'a') # a 追加模式
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)   #添加一个日志

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    # 很巧妙的二次封装
    def debug(self, message):               #调用 debug 函数 传入 message 然后引用 console 函数 传入 格式与内容
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)



    # def get_case_logger(self):  # 获取日志收集器
    #     return self.logger      #返回日志收集器

if __name__ == '__main__':
    log = HandleLogger()
    log.info("---测试开始----")
    log.info("输入密码")
    log.warning("----测试结束----")
