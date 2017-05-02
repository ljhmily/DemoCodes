#!/usr/bin/python3
# coding=utf-8

import urllib.request
import http.cookiejar


def makemyopener(head={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html; charset=utf-8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
}):
    cj = http.cookiejar.CookieJar()
    bopener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    bopener.addheaders = header
    return bopener

def saveFile(file):
    savePath = "tmp.log"
    f_obj = open(savePath, 'wb')
    f_obj.write(data)
    f_obj.close()

oper = makemyopener()
urlopen = oper.open('https://www.baidu.com', timeout=1000)
data = urlopen.read()
print(data.decode('utf-8'))
saveFile(data)