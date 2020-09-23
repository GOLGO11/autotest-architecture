import logging
import os
import sys

import time
from common.file_path import log_path


class LogTools(object):
    def __init__(self):
        self.logfile = os.path.join(log_path(), '%s.log' % self.nowtime())
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.format = logging.Formatter('[%(asctime)s]-[%(levelname)s]-%(message)s')
        self.log_current_name = str(sys._getframe().f_back.f_code.co_name)

    def __console(self, loglevel, message):
        fh = logging.FileHandler(self.logfile, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.format)
        self.logger.addHandler(fh)

        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        sh.setFormatter(self.format)
        self.logger.addHandler(sh)

        if loglevel == 'info':
            self.logger.info("".join(["run:", message]))
        elif loglevel == 'debug':
            self.logger.debug("".join(["run:", message]))
        elif loglevel == 'warning':
            self.logger.warning("".join(["run:", message]))
        elif loglevel == 'error':
            self.logger.error("".join(["run:", message]))
        self.logger.removeHandler(fh)
        self.logger.removeHandler(sh)
        fh.close()

    def info(self, message):
        self.__console('info', message)

    def debug(self, message):
        '''输出debug信息'''
        self.__console('debug', message)

    def warning(self, message):
        '''输出warning信息'''
        self.__console('warning', message)

    def error(self, message):
        '''输出error信息'''
        self.__console('error', message)

    def nowtime(self):
        '''获取当前时间'''
        nowtime = time.strftime("%Y-%m-%d")
        return nowtime

    def _logcurname(self):
        return str(sys._getframe().f_back.f_code.co_name)

# 调试代码
# if __name__ == '__main__':
#     log = LogTools()
#     log.info('nihao')
