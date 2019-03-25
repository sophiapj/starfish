#!/usr/bin/env python3
# -*- coding: utf-8 -*

'''
@Author: sophiapj
@Contact: sophiapj@163.com 
@File: ReadConfigini.py
@Desc: 读取配置文件的信息
'''
import configparser
import codecs
import os

class ReadConfigIni():
    '''
    实例化configparser
    '''

    def __init__(self,filename):
        self.cf = configparser.ConfigParser()
        self.cf.read(filename)

    #读操作
    def getConfigValue(self,config,name):
        value = self.cf.get(config,name)
        return value
