#@斐波那契数列
#@创建时间：2018-05-14
#@作者：mazhicheng

#!/usr/bin/python

x = 0
y = 1
z = 1
n_number = 0
times = []
f_list = [x]

try:
	n_number = int(input("\033[34;1m 请输入你想得到的斐波那契的个数：\033[0m"))
	if n_number < 0:
		print("\033[31;1m 请输入正整数！\033[0m")
	else:
		times = range(int(n_number/3)+1)
except ValueError:
	print("\033[31;1m 请输入正整数！\033[0m")
else:
	for i in times:
		z = x + y
		y = z + x
		x = y + z
		f_list.append(z)
		f_list.append(y)
		f_list.append(x)
if x == 0:
	pass
else:
	str_f_list = f_list[0:n_number]
	print('\033[32;1m 最后得到的数列为: {} \033[0m'.format(str_f_list))


