# !/usr/bin/evn python
# -*- coding:utf-8 -*-

"""
什么是水仙花数？百度一下：水仙花数是指一个 n 位正整数 ( n≥3 )，它的每个位上的数字的 n 次幂之和等于它本身。（例如：1^3 + 5^3+ 3^3 = 153）。
打印输出所有的"水仙花数"。
"""

import math

for i in range(100, 9999):
	bit = len(str(i))
	sum = 0
	num, remain = i % 10, i / 10
	while remain > 0 or num > 0 :	
		sum += math.pow(num, bit)
		num, remain = remain % 10, remain / 10

	if sum == i:
		print i

