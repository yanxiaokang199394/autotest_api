import logging
import logging.handlers
import os
import time


class logs(object):
    def __init__(self):
        self.logger = logging.getLogger("")
        # 设置输出的等级
        LEVELS = {'NOSET': logging.NOTSET,
                  'DEBUG': logging.DEBUG,
                  'INFO': logging.INFO,
                  'WARNING': logging.WARNING,
                  'ERROR': logging.ERROR,
                  'CRITICAL': logging.CRITICAL}
        logs_dir="log_data"
        if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
            pass
        else:
            os.mkdir(logs_dir)
        # 修改log保存位置
        timestamp=time.strftime("%Y%m%d",time.localtime())
        logfilename='%s_info.log' % timestamp
        logfilepath=os.path.join(logs_dir,logfilename)
        rotatingFileHandler = logging.handlers.RotatingFileHandler(filename =logfilepath,
                                                                   maxBytes = 1024 * 1024 * 50,
                                                                   backupCount = 5)
        # 设置输出格式
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        rotatingFileHandler.setFormatter(formatter)
        # 控制台句柄
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(formatter)
        # 添加内容到日志句柄中
        self.logger.addHandler(rotatingFileHandler)
        self.logger.addHandler(console)
        self.logger.setLevel(logging.INFO)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

if __name__ == '__main__':
    logger = logs()
    logger.info("this is info")
    logger.debug("this is debug")
    logger.error("this is error")
    logger.warning("this is warning")
    logger.critical("this is critical")