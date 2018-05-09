#!bin/python

########################################################################
#需求：一个数字加100是一个数的平方，再加168又是另一个数的平方，求这个数#
#创建时间：20180508                                                    #
#作者：mazhicheng                                                      #
########################################################################

import math
import re

x = list(range(100000))

for i in x:
	first_add_result = x[i] + 100
	first_add_result_sq = math.sqrt(first_add_result)
	first_myze = re.match('^[0-9]+.0+$', str(first_add_result_sq))
	
	if not first_myze is None:
		for j in x:
			second_add_result = x[j] + 268
			second_add_result_sq = math.sqrt(second_add_result)
			second_myze = re.match('^[0-9]+.0+$', str(second_add_result_sq))

			if not second_myze is None and x[i] == x[j]:
				print(x[j])
			else:
				pass
	else:
		pass

print('\033[31;1m 执行完成 ! \033[0m') 


