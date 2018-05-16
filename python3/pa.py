#!/usr/bin/python

#@need:pa
#@createdtime:20180515
#@author:mazhicheng

import requests, re
from bs4 import BeautifulSoup

need_to_pa_url = 'http://www.51testing.com/html/'
assum_my = {'user_agent':'Mozilla/5.0'}
url_list1 = []

#获取head
get_head = requests.head(need_to_pa_url)
body_head = get_head.headers
print('\033[33;1m 抓取head：\033[0m \033[32;1m {} \033[0m'.format(body_head))

#获取body
get_url = requests.get(url = need_to_pa_url, headers = assum_my)
get_url.encoding = get_url.apparent_encoding
body_result = get_url.text
print('\033[33;1m 抓取body：\033[0m \033[32;1m {} \033[0m'.format(body_result))

#过滤信息
filter_my = BeautifulSoup(body_result, 'html.parser')
url_result = filter_my.find_all('a')
for link in url_result:
	if re.match('http://www', str(link.get('href'))) != None:
		url_list1.append(link.get('href'))
	else:
		pass
#去重复
url_list1_set = set(url_list1)
url_list1_list = list(url_list1_set)

for i in range(len(url_list1_list)):
	print(url_list1_list[i])

print(len(url_list1_list))

#二级url爬取
two_count = 0
for i in range(len(url_list1_list)):
	try:
		two_get_url = requests.get(url = url_list1_list[i], headers = assum_my, timeout = 5 )
	except requests.exceptions.ConnectionError:
		pass
	except requests.exceptions.ReadTimeout:
		pass
	else:
		two_get_url.encoding = two_get_url.apparent_encoding
		two_body_result = two_get_url.text
		print('\033[33;1m 抓取body：\033[0m \033[32;1m {} \033[0m'.format(two_body_result))
		two_count += 1 

#参考信息
print('_____________________________________________')
print()
print('\033[33;1m一级页面获取到的url数量：\033[0m', len(url_list1_list))
print('\033[33;1m一级页面获取到并访问成功的url数量：\033[0m', two_count)
print('\033[33;1m二级页面的访问成功率：\033[0m', round(two_count/len(url_list1_list), 2) * 100, '%')
print('_____________________________________________')
