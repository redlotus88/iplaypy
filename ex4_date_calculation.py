#coding=utf-8

"""
简述：要求输入某年某月某日
提问：求判断输入日期是当年中的第几天？
"""
import time

time_input = input('请输入日期格式为yyyy-mm-dd：')
 
date = time.strptime(time_input, '%Y-%m-%d') #python3
print("输入的日期[%s] 是当年中的第[%d]天" % (time.strftime('%Y-%m-%d'), date.tm_yday))