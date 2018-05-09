#!bin/python

##############################
#需要：正则表达式测试        
#创建时间：20180509          
#作者：mazhicheng            
##############################


import re

input_str = str(input('\033[32;1m ---请输入你要测试的文字--- \033[0m'))
print('你需要测试的文字是：%s' % input_str)

while True:
	input_pattern = str(input('\033[32;1m ---请输入你的正则表达式--- \033[0m'))
	match_result = re.findall(input_pattern, input_str)
	if match_result:
		print('\033[34;1m 正则表达式匹配的结果是：%s\033[0m' % match_result)
		break
	else:
		if_exit = input('\033[31;1m 没有匹配到！是否继续？继续输入 ‘g’,退出输入非g: \033[0m')
		if if_exit == 'g':
			pass
		else:
			break

