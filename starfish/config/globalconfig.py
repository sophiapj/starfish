#!/usr/bin/env python3
# -*- coding: utf-8 -*

'''
@Author: sophiapj
@Contact: sophiapj@163.com
@File: __init__.py
@Desc:
'''

import os
from public.common.ReadConfigini import ReadConfigIni

#读取配置文件
#获取configini的路径
file_path = os.path.split(os.path.realpath(__file__))[0]

#读取配置文件
read_config = ReadConfigIni(os.path.join(file_path,"config.ini"))

#通过config.ini获取项目参数
project_path = read_config.getConfigValue("project","project_path")

#日志路径
log_path = os.path.join(project_path,"report","Log")

#测试用例路径
TestCase_path = os.path.join(project_path,"testcases")

#测试报告路径
report_path = os.path.join(project_path,"report","TestReport")

#测试数据路径
data_path = os.path.join(project_path,"Data","TestData")