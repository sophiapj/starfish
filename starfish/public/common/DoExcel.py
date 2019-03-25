#!/usr/bin/env python3
# -*- coding: utf-8 -*

'''
@Author: sophiapj
@Contact: sophiapj@163.com 
@File: DoExcel.py
@Desc: 读取Excel数据，实现数据驱动测试
'''

import xlrd
import os

class ReadExcel():
    '''
    打开Excel，读取测试数据
    '''

    #打开Excel
    def __init__(self,filename,sheetname):
        self.workbook = xlrd.open_workbook(filename)
        self.sheetName = self.workbook.sheet_by_name(sheetname)

    #获取某个单元格的数据
    def read_excel(self,rownum,colnum):
        value = self.sheetName.cell(rownum,colnum)
        return value
