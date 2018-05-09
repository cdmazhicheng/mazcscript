#!/usr/myvirtualenv/python3small/bin/python

############################################################
#需求说明：通过利润来计算收入，每个利润金额端的收入比例不同#
#创建时间：20180508                                        #
#作者:mazhicheng                                           #
############################################################

import re

bonus = input("请输入利润：")
wan = 10000

if not re.findall('^[0-9]+$', bonus):
	print(' \033[31;1m  请输入整数！ \033[0m ')
else:
	bonus = int(bonus)
	print('你输入的是：', bonus)
	if bonus <= 10*wan :
        	results = bonus * 0.1
        	print("收入为：", results)
	elif bonus > 10*wan and bonus <= 20*wan:
        	results = (bonus-10*wan)*0.075 + 10*wan*0.1
        	print("收入为：", results)
	elif bonus > 20*wan and bonus <= 40*wan:
        	results = (bonus-20*wan)*0.05 + 10*wan*0.075 + 10*wan*0.1
        	print("收入为：", results)
	elif bonus > 40*wan and bonus <= 60*wan:
        	results = (bonus-40*wan)*0.03 + 20*wan*0.05 + 10*wan*0.075 + 10*wan*0.1
        	print("收入为：", results)
	elif bonus > 60*wan and bonus <= 100*wan:
        	results = (bonus-60*wan)*0.015 + 20*wan*0.03 + 20*wan*0.05 + 10*wan*0.075 + 10*wan*0.1
        	print("收入为：", results)
	elif bonus >100*wan:
        	results = (bonus-100*wan)*0.001 + 40*wan*0.015 + 20*wan*0.03 + 20*wan*0.05 + 10*wan*0.075 + 10*wan*0.1
        	print("收入为：", results)
	else:
        	pass

