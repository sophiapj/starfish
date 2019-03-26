#!/usr/bin/env python3
# -*- coding: utf-8 -*

'''
@Author: sophiapj
@Contact: sophiapj@163.com 
@File: TestCaseInfo.py
@Desc:
'''

class TestCaseInfo():
    '''
    测试用例的信息
    '''
    def __init__(self,id="",name="",owner="",result="",starttime="",endtime="",secondsDuration="",erroinfo=""):
        self.id = id
        self.name = name
        self.owner = owner
        self.result = result
        self.starttime = starttime
        self.endtime = endtime
        self.secondsDuration = secondsDuration
        self.erroinfo = erroinfo