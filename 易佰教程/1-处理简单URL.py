#!/usr/bin/python3
# coding=utf-8

import urllib
import urllib.request, urllib.parse

data = {}
data['word'] = 'Jecvay Notes'

url_values = urllib.parse.urlencode(data)
url = "http://www.baidu.com/s?"
full_url = url + url_values

data = urllib.request.urlopen(full_url).read()
data = data.decode('utf-8')

print(data)
