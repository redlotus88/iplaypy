#coding=utf-8
"""
整数顺序排列问题简述：任意三个整数类型，x、y、z
提问：要求把这三个数，按照由小到大的顺序输出
"""

x = input('请输入整数x:')
y = input('请输入整数y:')
z = input('请输入整数z:')

#判断是否是整数：
for i in (x, y, z):
	if type(x) != int:
		raise TypeError('%s 不是整数' % str(x))

a = list([x, y, z])
a.sort()
print('排序后的结果为：%s' % a)	

