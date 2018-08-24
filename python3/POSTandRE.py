
import requests

#get方式测试
url = 'http://www.ytny.demo/sjytadmin/index.php/auth/login'
testuser = requests.get(url)
print(testuser.text)