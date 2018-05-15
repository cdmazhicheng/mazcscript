#!/usr/bin/python

#@need:pa
#@createdtime:20180515
#@author:mazhicheng

import requests

need_to_pa_url = 'https://www.baidu.com/'
assum_my = {'user_agent':'Mozilla/5.0'}
#获取head
get_head = requests.head(need_to_pa_url)
body_head = get_head.headers
print('\033[33;1m 抓取head：\033[0m \033[32;1m {} \033[0m'.format(body_head))

#获取body
get_url = requests.get(url = need_to_pa_url, headers = assum_my)
get_url.encoding = get_url.apparent_encoding
body_result = get_url.text
print('\033[33;1m 抓取body：\033[0m \033[32;1m {} \033[0m'.format(body_result))

#参考信息
print('_____________________________________________')
print()
print('\033[33;1m从header中判断的编码方式：\033[0m', get_url.encoding)
print('\033[33;1m从内容中判断的编码方式：\033[0m', get_url.apparent_encoding)
print('\033[33;1m请求的返回状态：\033[0m', get_url.status_code)
print('_____________________________________________')
