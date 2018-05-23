#!/usr/bin/python

#@filename: mainrun.py
#@类说明：主函数

from get_body import GetBody
from get_link import GetLink
import sys

#获取电影名称
get_body_object = GetBody()
one_body = get_body_object.get_body('https://www.lookpian.com/dianying/index.html')

get_link_object = GetLink()
one_link = get_link_object.get_link(one_body)

one_link_sp = []
for i in range(len(one_link)):
	one_link_sp.append(one_link[i].split('-----'))

print()
print('\033[32;1m已为您爬取到如下影片：\033[0m')
for i in range(len(one_link_sp)):
	sys.stdout.write('【{}】{}  '.format(i+1, (one_link_sp[i][0])))
print('\r')

#下载制定影片
ready_video = input('\033[31;1m请输入您需要下载的影片序号：\033[0m')
ready_video_number = int(ready_video)

print('你选择的影片《{}》......'.format(one_link_sp[ready_video_number-1][0]))
print('播放地址{}'.format(one_link_sp[ready_video_number-1][1]))
print('\r')



