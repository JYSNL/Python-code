'''import urllib.request

response = urllib.request.urlopen('http://www.4399.com')
html = response.read()
print(html)

import urllib.request
import urllib.parse

data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding = 'utf8')
response = urllib.request.urlopen('http://www.4399.com',data = data)
html = response.read()
print(html)

import urllib3
http = urllib3.PoolManager()
response = http.request('GET','http://www.4399.com/')
print(response.data)'''

import requests
'''
response = requests.get('http://www.baidu.com')
print(response.status_code)
print(response.url)
print(response.headers)
print(response.cookies)
print(response.text)
print(response.content)

payload = {'key1':'value1','key2':'value2'}
response = requests.get("http://httpbin.org/get",params=payload)
print(response)
'''
url = 'http://www.baidu.com/'
headers = {'User-Agent':
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}
response = requests.get(url,headers = headers)
print(response.content)