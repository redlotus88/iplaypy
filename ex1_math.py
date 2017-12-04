""""
Python练习题问题如下：
简述：这里有四个数字，分别是：1、2、3、4
提问：能组成多少个互不相同且无重复数字的三位数？各是多少？
"""

"""
result = 0 
for x in range(1, 5):
	for y in range(1, 5):
		for z in range(1, 5):
			if (x != y and y != z and x != z) :
				print('%d %d %d' % (x, y, z))
				result += 1
print(result)
"""


result = []

def func(x, y, z) :
	print(x, y, z)
	return 1

result = [
func(x, y, z)
for x in range(1,5) 
for y in range(1,5) 
for z in range(1,5)
if x != y and y != z and z != x
]

total = 0
for i in result: 
	total += 1
print(total)

