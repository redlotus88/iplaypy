#coding=utf-8
"""
斐波那契数列（Fibonacci sequence），又称黄金分割数列、因数学家列昂纳多·斐波那契以兔子繁殖为例子而引入，
故又称为“兔子数列”，指的是这样一个数列：1、1、2、3、5、8、13、21、34、在数学上，斐波纳契数列以如下被以递归的方法定义。
F0 = 0
F1 = 1
Fn = F[n-1] + F[n-2]
要求一：输出第10个斐波那契数列
"""

fib_dict = {}

def fibonacci(n):
	if fib_dict.has_key(n) :
		return fib_dict[n]

	result = 0
	if n < 1:
		result = 0
	elif n == 1:
		result = 1
	else :
		result = fibonacci(n-1) + fibonacci(n-2)
	fib_dict[n] = result
	return result

if __name__ == '__main__':
	print("输出第10个斐波那契数列：%s" % fibonacci(10))
	print(fib_dict.values())
