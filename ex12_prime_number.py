# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
简述：区间范围101-200
要求：判断这个区间内有多少个素数，并逐一输出.
"""

import math

for i in range(101, 200):
	isPrime = True
	for j in range(2, int(math.sqrt(i)) + 1):
		if i % j == 0 :
			isPrime = False
			break

	if isPrime:
		print(i)




