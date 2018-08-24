#!/usr/bin/python

#@need:patext
#@created_time:20180515
#@author:mazhicheng

import requests, sys
from bs4 import BeautifulSoup

'''
类说明：下载网络小说

'''

class downloader(object):

	def __init__(self):
		self.server = 'http://www.biqukan.com/'
		self.target = 'http://www.biqukan.com/1_1094/'
		self.names = []
		self.urls = []
		self.nums = 0

#函数说明：获取下载链接

	def get_download_url(self):
		req = requests.get(url = self.target)
		html = req.text
		div_bf = BeautifulSoup(html)
		div = div_bf.find_all('div', class_ = 'listmain')
		a_bf = BeautifulSoup(str(div[0]))
		a = a_bf.find_all('a')
		self.nums = len(a[15:])
		for each in a[15:]:
			self.names.append(each.string)
			self.urls.append(self.server + each.get('href'))

#函数说明：获取章节内容

	def get_contents(self, target):
		req = requests.get(url = target)
		html = req.text
		bf = BeautifulSoup(html)
		texts = bf.find_all('div', class_ = 'showtxt')
		texts = texts[0].text.replace('\xa0'*8, '\n\n')
		return texts

#函数说明：将获取的内容写入文件

	def writer(self, name, path, text):
		writer_flag = True
		with open(path, 'a', encoding= 'utf-8') as f:
			f.write(name + '\n')
			f.writelines(text)
			f.write('\n\n')

#函数说明：下载

if __name__ == '__main__':
	dl = downloader()
	dl.get_download_url()
	print("开始下载：")
	for i in range(dl.nums):
		dl.writer(dl.names[i], 'yinianyongheng.txt', dl.get_contents(dl.urls[i]))
		sys.stdout.write("已下载：%.3f%%" % float(i/dl.nums) + '\r')
		sys.stdout.flush()
	print("下载完成！")
