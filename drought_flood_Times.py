#coding:utf-8
import numpy as np
import os
import sys
import xlrd
import datetime
import glob

from DrawPic import *

def Main():
    filename = ur'D:\wanjin\宁夏降水数据\年降水量分析.xlsx'
    readbook = xlrd.open_workbook(filename)

    print(readbook.sheet_names())
    # sheet = readbook.sheet_by_name(u'降水量')
    sheet = readbook.sheet_by_index(1)

    waterofyear =  sheet.col_values(1)[1:61]
    strtime =  sheet.col_values(0)[1:61]

    strDate = [datetime.datetime.strptime(str(int(i)), "%Y") for i in strtime]

    Draw_Yearofwater(filename.replace('.xlsx', '.png'), strDate, waterofyear)

if __name__ == '__main__':

    Main()







