#!/usr/bin/python

#@need:pa pictrues
#@createddate:20180517
#@author:mazhicheng

import requests, re, os
from bs4 import BeautifulSoup
import urllib.request

class Pa_picture(object):

	#初始化数据
	def __init__(self):
		self.one_layer_url = 'http://www.ivsky.com/'
		self.pretend_mine = {'user_agent':'Mozilla/5.0'}
		self.one_link = []
		self.two_link = []
		self.two_layer_body = ''

		self.one_layer_number = 0
		self.two_layer_number = 0

	#取出首页的body
	def get_one_layer_body(self):
		one_layer_url = requests.get(url = self.one_layer_url, headers = self.pretend_mine )
		one_layer_url.encoding = one_layer_url.apparent_encoding
		one_layer_body = one_layer_url.text
		return one_layer_body

	#取出首页的第一层链接
	def get_one_link(self):
		one_link_all = BeautifulSoup(self.get_one_layer_body(), 'html.parser')
		one_link_list = one_link_all.find_all('a')
		for one_link in one_link_list:
			if re.match('/bizhi/',str(one_link.get('href'))) != None:
				self.one_link.append('http://www.ivsky.com' + one_link.get('href'))
			else:
				pass
		#去重复
		self.one_link_set = set(self.one_link)
		self.one_link_list = list(self.one_link_set)
		#输出第一层的链接列表
		for i in range(len(self.one_link_list)):
			print('\033[33;1m 第一层链接：\033[0m {}'.format(self.one_link_list[i]))
		self.one_layer_number = len(self.one_link_list)
		return self.one_link_list

	#取出第一层链接的所有body合成一个body
	def get_two_layer_body(self):
		for i in range(len(self.get_one_link())):
			two_layer_url = requests.get(url = self.get_one_link()[i], headers = self.pretend_mine)
			two_layer_url.encoding = two_layer_url.apparent_encoding
			self.two_layer_body += two_layer_url.text
		return self.two_layer_body

	#取出第二层链接
	def get_two_link(self):
		two_link_all = BeautifulSoup(self.get_two_layer_body(), 'html.parser')
		two_link_list = two_link_all.find_all('a')
		for two_link in two_link_list:
			if re.match('/bizhi/',str(two_link.get('href'))) != None:
				self.two_link.append('http://www.ivsky.com' + two_link.get('href'))
			else:
				pass
		#去重复
		self.two_link_set = set(self.two_link)
		self.two_link_list = list(self.two_link_set)
		#输出第二层的链接列表
		for i in range(len(self.two_link_list)):
			print('\033[34;1m 第二层链接：\033[0m {}'.format(self.two_link_list[i]))
		self.two_layer_number = len(self.two_link_list)

	#统计
	def info_result(self):
		print('------------------------------------------')
		print('第一层的爬取到url链接数量为：{}'.format(self.one_layer_number))
		print('第二层的爬取到url链接数列为：{}'.format(self.two_layer_number))
		print('------------------------------------------')

if __name__ == '__main__':
	pa = Pa_picture()
	pa.get_two_link()
	pa.info_result()

