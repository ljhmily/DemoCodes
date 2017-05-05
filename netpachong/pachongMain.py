#!/usr/bin/python3

from netpachong.pachongBase import *
from netpachong.pachongListComics import *

url = "http://www.xeall.com/shenshi"
path = "temp"
cmc = Comics(url, path)
cmc.main()
