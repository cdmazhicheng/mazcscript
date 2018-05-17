#!/usr/bin/python

#@need:pa pictrues
#@createddate:20180517
#@author:mazhicheng

import requests, re, os
from bs4 import BeautifulSoup
import urllib.request

class Pa_picture(object):

	def __init__(self):
		self.one_layer_url = 'http://desk.zol.com.cn/'
		self.pretend_mine = {'user_agent':'Mozilla/5.0'}
		self.one_layer_images_list = []

	def get_one_layer_body(self):
		one_layer_url = requests.get(url = self.one_layer_url, headers = self.pretend_mine )
		one_layer_url.encoding = one_layer_url.apparent_encoding
		one_layer_body = one_layer_url.text
		#print(one_layer_body)
		return one_layer_body

	def get_one_layer_images(self):
		one_layer_all = BeautifulSoup(self.get_one_layer_body(), 'html.parser')
		one_layer_images = one_layer_all.find_all('img')
		#print(one_layer_images) 
		for link in one_layer_images:
			if re.match('https://',str(link.get('srch'))) != None:
				self.one_layer_images_list.append(link.get('srch'))
			else:
				pass
		self.one_layer_images_list_set = set(self.one_layer_images_list)
		self.one_layer_images_list_list= list(self.one_layer_images_list_set)
		for i in range(len(self.one_layer_images_list_list)):
			print(self.one_layer_images_list_list[i])
		return self.one_layer_images_list_list

	def down_images(self):
		if not os.path.exists('/usr/myimages'):
			os.makedirs('/usr/myimages')
		for i in range(len(self.get_one_layer_images())):
			urllib.request.urlretrieve(self.get_one_layer_images()[i],'/usr/myimages/{}.jpg'.format(i) )




if __name__ == '__main__':
	pa = Pa_picture()
	pa.down_images()

