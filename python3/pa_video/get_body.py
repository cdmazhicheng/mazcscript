#!/usr/bin/python

#@filename:get_body.py
#类说明：获取电影名字及第一层url地址

import requests

class GetBody:
	
	def __init__(self):
		self.pretend_mine = {'user_agent': 'Mozilla/5.0'}

	def get_body(self, url ):
		one_url = requests.get(url, headers = self.pretend_mine)
		one_url.encoding = one_url.apparent_encoding
		one_body = one_url.text
		return one_body

