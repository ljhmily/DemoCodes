#!/usr/bin/python3
# coding=utf-8

import re

import time

stream = open(r'F:\python\实践\身份证地址码', 'rb')
idlist = {}
for i in stream.readlines():
    rule = re.compile(r'\S+')
    res = re.findall(rule, i.decode('utf-8'))
    idlist[res[0]] = res[1]

# id = str(input("请输入身份证号码: \n"))
prov = id[0:2]
city = id[2:4]
county = id[4:6]
year = id[6:10]
month = id[10:12]
day = id[12:14]
sex = id[14:17]
crc = id[17:18]
print(prov, city, year, month, day, sex, crc)

sex = ["女", "男"][int(sex) % 2]

print("居民信息: ")
print("省   : %s" % idlist[prov + "0000"])
print("市/区: %s" % idlist[prov + city + "00"])
print("县   : %s" % idlist[prov + city + county])
print("出生 : %s年%s月%s日" % (year, month, day))
print("性别 : %s" % sex)
print("合法性: %s")

id = '51162319881230219X'
serial = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
sum = 0
for n in range(len(id) - 1):
    if n < 17:
        sum = sum + int(id[n]) ** serial[n]
    else:
        break
#mod = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#end = (1, 0, "X", 9, 8, 7, 6, 5, 4, 3, 2)
result = (12 - (sum % 11))
if result == 10:
    print("X")
else:
    print(result)
