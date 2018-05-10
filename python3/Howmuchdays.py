#!/bin/python
#@需求：输入日期能够自动计算是当年的第多少天
#@作者：mazhicheng
#@创建时间：2018-05-10


import datetime
import re

input_date = input('请输入你要计算的日期（格式 1964-7-11）：')
re_date = re.findall('[0-9]+', input_date)
try:
	year_days_first = datetime.date(int(re_date[0]), 1, 1)
except ValueError:
	print('输入的格式不正确，请重新输入！')
except IndexError:
	print('输入的格式不正确，请重新输入！')
else:
	try:	
		year_days_last = datetime.date(int(re_date[0]), int(re_date[1]), int(re_date[2]))
	except ValueError:
		print('输入的格式不正确，请重新输入！')
	except IndexError:
		print('输入的格式不正确，请重新输入！')
	else:
		how_days = str(year_days_last.toordinal() - year_days_first.toordinal())
		print('这是 %s' %re_date[0],'年的第 \033[34;1m %s \033[0m' %how_days,'天')

