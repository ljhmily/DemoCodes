#!/usr/bin/python3
#coding=utf-8

import urllib.request

url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
data = data.decode('utf-8')
print(data)