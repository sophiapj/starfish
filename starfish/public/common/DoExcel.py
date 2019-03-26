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
from xlutils.copy import copy

data_path = os.path.split(os.path.realpath(__file__))[1]
#data_excel = os.path.join(data_path, "TestData")


class ReadExcel():

    def __init__(self, filename, sheetname):

        self.Filename = os.path.join(data_path, filename)
        self.workbook = xlrd.open_workbook(self.Filename) # 打开Excel
        self.sheetName = self.workbook.sheet_by_name(sheetname)

    def get_row_num(self, cols_num, case_id):
        '''
        作用：返回case_id所在的行号
        :param cols_num:检索那一列
        :param case_id:
        :return: 返回行号
        '''
        cols = self.sheet.col_values(cols_num)

        colnum = 0
        for col_data in cols:
            if col_data == case_id:
                break
            colnum += 1
        return colnum  # 自增后，返回case_id所在的行

    def get_rowline_data(self, row):
        '''
        作用：根据get_row_num返回的行号，获取某行的值
        :param row: 传递行号,在get_row_num中返回的行号
        :return:
        '''
        rowline_data = self.sheet.row_values(row)
        return rowline_data  # 某行的数据

    # 获取某个单元格的数据
    def read_excel(self, rownum, colnum):
        value = self.sheetName.cell(rownum, colnum).value
        return value

    def write_excel(self, sheetnum, row, col, value):
        '''
        作用：向单元格中写入数据
        :param sheetnum: sheet的编号，从0开始
        :param row: 行号
        :param col: 列号
        :param value: 值
        :return:
        '''

        newworkbook = xlrd.open_workbook(self.Filename)
        # 拷贝Excel
        newbook = copy(newworkbook)
        sheet = newbook.get_sheet(sheetnum)

        sheet.write(row, col, value)
        newbook.save(self.Filename)
