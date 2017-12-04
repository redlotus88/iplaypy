#coding=utf8
"""
简述：一个整数，它加上100和加上268后都是一个完全平方数
提问：请问该数是多少？
"""

import math

for i in range(0, int(math.pow(268, 2))) :
	num1 = math.sqrt(i + 100)
	num2 = math.sqrt(i + 268)
	if int(num1) == num1 and int(num2) == num2:
		print ('[ %d ]加上100和加上268后都是一个完全平方数' % i)

