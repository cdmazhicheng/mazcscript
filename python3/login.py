#login

name = 'mazhicheng'
password = '123456'

input_name = input('输入账号：')
input_pawd = input('输入密码：')

if input_name != name or input_pawd != password:
	print('账号和密码不正确！')
else:
	print('登录成功！')
	

