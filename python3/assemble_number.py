#!/usr/myvirtualenv/python3small/bin/python


##################################################################################
# 需求说明：此方法是输入数字，看能够通过这些输入的数字产生多少个3位数，且不重复. 
# 创建日期：20180504                                                             
# 作者：makunjie                                                                 
##################################################################################


def assemble():
	intnumber = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	number = input('请输入一组整数:')
	numbers = list(map(str, str(number)))
	intnumberset = set(intnumber)
	numbersset = set(numbers)
	#判断是否为整数
	if not numbersset.issubset(intnumberset):
		print('你输入的不是整数，系统退出!')
	else:
		zhuhelist = []
                #循环取数
		for i in numbers:
			number1 = str(i)
			for i in numbers:
                		number2 = str(i)
                		for i in numbers:
                        		number3 = str(i)
                        		zhuhestr = number1+number2+number3
                        		zhuhelist.append(zhuhestr)
        	#转换为集合是为了删除重复的元素
		zhuheset = set(zhuhelist)
		return print(
			' ***********包含以下数字：', zhuheset, '\n', 
			'***********总共数量：', len(zhuheset)
			)
#调用方法	
assemble()
#测试模块
print('\033[31;1m 调试中...... \033[0m')


