#!/usr/bin/python

#@类：获取body中的link链接
#@文件名：getlink.py
#@创建时间：20180521
#@作者：mazhicheng

from bs4 import BeautifulSoup
import re

#类解释：输入一个url地址的body内容（url_body_content）, 输出符合筛选条件的link链接地址列表（link_selected_list）
class GetLink:

	def __init__(self):
		self.link_selected = []

	def get_link(self, url_body_content):
		get_link_all = BeautifulSoup(url_body_content, 'html.parser')
		get_link_select = get_link_all.find_all('a')
		for get_link in get_link_select:
			if re.match('/bizhi/', str(get_link.get('href'))) != None:
				self.link_selected.append('http://www.ivsky.com' + get_link.get('href'))
			else:
				pass
		link_selected_set = set(self.link_selected)
		link_selected_list = list(link_selected_set)
		return link_selected_list

