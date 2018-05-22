#!/usr/bin/python

#@类：获取url链接的body
#@文件名：getbody.py
#@创建时间：20180521
#@作者：mazhicheng

import requests


#类解释：输入一个url地址（urladdr）,返回这个url地址body中的全部内容（url_body_content）
class GetBody:

	def __init__(self):
		self.pretend_mine = {'user_agent': 'Mozilla/5.0'}
 
	def get_body(self, urladdr):
		url_body = requests.get(urladdr, headers = self.pretend_mine)
		url_body.encoding = url_body.apparent_encoding
		url_body_content = url_body.text
		return url_body_content


