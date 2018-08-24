#!/usr/bin/python

#@need:pa_modify
#@createddate:20180516
#@author:mazhicheng

import requests, re
from bs4 import BeautifulSoup

class Pawebs(object):

	def __init__(self):
		self.one_layer_url = 'http://www.51testing.com/html/'
		self.pretend_mine = {'user_agent':'Mozilla/5.0'}
		self.two_layer_url_list = []
		self.error_url = []

	#方法：获取第一层url的body
	def get_one_body(self):
		get_one_url = requests.get(url = self.one_layer_url, headers = self.pretend_mine)
		get_one_url.encoding = get_one_url.apparent_encoding
		one_body = get_one_url.text
		return one_body
		#print('\033[33;1m 抓取head：\033[0m \033[32;1m {} \033[0m'.format(one_body))

	#方法：过滤第一层urlbody中的url地址做为第二次urls
	def filter_one_body(self):
		filter_one_body = BeautifulSoup(self.get_one_body(), 'html.parser')
		filter_a_tag = filter_one_body.find_all('a')
		for link in filter_a_tag:
			if re.match('http://www', str(link.get('href'))) != None:
				self.two_layer_url_list.append(link.get('href'))
			else:
				pass
		#删除掉重复的url地址
		two_layer_url_list_set = set(self.two_layer_url_list)
		two_layer_url_list_list = list(two_layer_url_list_set)
		#for i in range(len(two_layer_url_list_list)):
			#print(two_layer_url_list_list[i])
		return two_layer_url_list_list

	#方法：第二次爬取网页
	def get_two_body(self):
		self.two_layer_count = 0
		for i in range(len(self.filter_one_body())):
			try:
				get_two_url = requests.get(url = self.filter_one_body()[i], headers = self.pretend_mine, timeout = 5)
			except requests.exceptions.ConnectionError:
				self.error_url.append('ConnectionError:' + self.filter_one_body()[i])
				pass
			except requests.exceptions.ReadTimeout:
				self.error_url.append('ReadTimeoutError:' + self.filter_one_body()[i])
				pass
			else:
				get_two_url.encoding = get_two_url.apparent_encoding
				two_body = get_two_url.text
				print('\033[33;1m 抓取body：\033[0m \033[32;1m {} \033[0m'.format(two_body))
				self.two_layer_count += 1
		return self.two_layer_count

	#方法：统计结果
	def info(self):
		self.two_number = len(self.filter_one_body())
		self.two_number_success = self.get_two_body()
		print('-----------------------------------------------------------------')
		print()
		print('\033[33;1m一级页面获取到并访问成功的url数量：\033[0m', self.two_number_success)
		print('\033[33;1m一级页面获取到的url总数量：\033[0m', self.two_number)
		print('\033[33;1m二级页面的访问成功率：\033[0m', round(self.two_number_success/self.two_number, 2) * 100, '%')
		for i in range(len(self.error_url)):
			print(self.error_url[i])
		print('-----------------------------------------------------------------')

if __name__ == '__main__':
	pa = Pawebs()
	pa.info()

