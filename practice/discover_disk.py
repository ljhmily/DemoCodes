#!/usr/bin/python3
# coding=utf-8

import os, sys, re, json

file = "F:\python\实践\disk_stat"

data = open(file, 'r')
array = []
for line in data.readlines():
    disk = {}
    c = re.compile(r'\s+')
    ru = c.split(line)
    disk["{#DISK}"] = ru[2]
    disk["{#DISKDEV}"] = "/dev/" + ru[2]
    disk["{#DMNAME}"] = ru[2]
    disk["{#VMNAME}"] = ""
    disk["{#VMID}"] = ""
    #array.append(sorted(disk.items(), key=lambda e:e[0]))
    array.append(disk)
print(json.dumps({"data": array}))
