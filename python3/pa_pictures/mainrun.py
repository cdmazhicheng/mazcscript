#!/usr/bin/python

#@类：执行的主程序
#@文件名：mainrun.py
#@创建时间：20180521
#@作者：mazhicheng

from getbody import GetBody
from getlink import GetLink
import time, sys

#获取第一层的link
onegetbody = GetBody()
one_body = onegetbody.get_body('http://www.ivsky.com/')

onegetlink = GetLink()
one_link_selected = onegetlink.get_link(one_body)
for i in range(len(one_link_selected)):
	print('第一层link:', one_link_selected[i])

#获取第二层的link
two_body = ''
twogetbody = GetBody()
for i in range(len(one_link_selected)):
	two_body += twogetbody.get_body(one_link_selected[i])
	sys.stdout.write('\r')
	sys.stdout.write('\033[34;1m爬取中...%s\033[0m' %float(i/len(one_link_selected)))
	sys.stdout.flush()

twogetlink = GetLink()
two_link_selected = twogetlink.get_link(two_body)
for i in range(len(two_link_selected)):
	print('第二层link:', two_link_selected[i])

#统计
print('\033[31;1m第一层的link数量：\033[0m', len(one_link_selected))
print('\033[31;1m第二层的link数量：\033[0m', len(two_link_selected))
