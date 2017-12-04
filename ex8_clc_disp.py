#coding=utf-8
"""
简述：9*9乘法口诀表。
要求：逐项单位输出。例如1的一行，2的一行，以此类推。
"""
from __future__ import print_function

row = range(1, 10)
col = range(1, 10)

for r in row:
	for c in col:
		if r < c:
			continue
		else :
			print('%s * %s = %s\t' % (c, r, c*r), end='')
	print()



