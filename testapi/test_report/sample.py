
"""
@Version: 1.0
@Project: BeautyReport
@Author: Raymond
@Data: 2017/11/17 下午3:48
@File: sample.py
@License: MIT
"""
import unittest

from BeautifulReport import BeautifulReport

from qhsp.test_case.test_community import TestCommunity
from qhsp.test_case.test_login import TestLogin

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestLogin))
    result = BeautifulReport(suite)
    result.report(filename='测试报告', description='前台-登录', log_path='')
