#coding=utf-8
"""
提问：将一个列表的数据复制到另一个列表中。
"""

def copy(l):
	new_list = l[:]
	return new_list

l = [1,2,3,4,5]

print('原数组：%s' % l)
print('copy list to another one:')
copy_list = copy(l)
print(copy_list)
print('修改copy数组第2个元素为7:')
copy_list[1] = 7
print('两数组如下：')
print(l)
print(copy_list)


