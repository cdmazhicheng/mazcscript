#!/bin/python

#@demand：输入3个数，有小到大排序
#@author:mazhicheng
#@date:2018/05/11

three_number = range(3)
input_number = []
for i in three_number:
	try:
		input_number_util = float(input('请输入第 %s 个数：' % str(i+1)))
	except ValueError:
		print('输入的值有问题，请输入数字！')
		break
	else:
		input_number.append(input_number_util)

if len(input_number) < 3:
	pass
else:
	print('\033[34;1m 由小到大排序为：\033[0m', sorted(input_number))


