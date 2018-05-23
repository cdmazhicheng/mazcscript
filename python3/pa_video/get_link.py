#!/usr/bin/python

#@filename:get_link.py
#@类说明：从body中获取需要的link

from bs4 import BeautifulSoup
import re

class GetLink:
	
	def __init__(self):
		self.one_link = []
		self.one_name = []

	def get_link(self, url_body):
		one_url_body = BeautifulSoup(url_body, 'html.parser')
		one_url_link = one_url_body.find_all('a')

		for i in range(len(one_url_link)):
			if re.match('<a class="videopic lazy"', str(one_url_link[i])) != None:
				self.one_link.append(one_url_link[i].get('title') + '-----' + 'https://www.lookpian.com' +  one_url_link[i].get('href'))
			else:
				pass

		one_link_set = set(self.one_link)
		one_link_list= list(one_link_set)

		return one_link_list





