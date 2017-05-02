#!/usr/bin/python3
# coding=utf-8

import urllib.request

url = 'http://www.baidu.com'
req = urllib.request.Request(url, headers={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html; charset=utf-8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
})

urlopen = urllib.request.urlopen(req)
data = urlopen.read()
print(data.decode('utf-8'))
