#!/usr/bin/env python3
# -*- coding: utf-8 -*

'''
@Author: sophiapj
@Contact: sophiapj@163.com 
@File: Log.py
@Desc:封装对日志的操作
'''

import logging
import os
import time

class Logger():

    def __init__(self,logger,CmdLevel,FileLevel):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)')

        #设定日志文件的名称
        self.LogFileName = os.path.join("{0}.log".format(time.strftime("%Y-%m-%d")))

        #设置控制台日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(CmdLevel)

        #设置文件日志
        fh = logging.FileHandler(self.LogFileName)
        fh.setFormatter(fmt)
        fh.setLevel(FileLevel)

        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self,message):
        self.logger.debug(message)

    def info(self,message):
        self.logger.info(message)

    def war(self,message):
        self.logger.warning(message)

    def error(self,message):
        self.logger.error(message)

    def cri(self,message):
        self.logger.critical(message)