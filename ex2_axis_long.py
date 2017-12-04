# -*- coding:utf-8 -*-
"""
Python数轴、长整型，编程练习题实例二

简述：企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成.
提问：从键盘输入当月利润I，求应发放奖金总数？
"""

profit = int(input("输入利润："))

profitLimit = [0, 100000, 200000, 400000, 600000, 1000000]
profitDrawing = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
bonus = 0

for i in range(len(profitLimit) - 1, -1, -1):
	if (profit > profitLimit[i]) :
		bonus += (profit - profitLimit[i]) * profitDrawing[i]
		profit = profitLimit[i]

print("bonus: %d" % bonus)

