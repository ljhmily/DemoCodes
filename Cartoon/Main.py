#coding:utf-8

from DemoCodes.Cartoon.Comic import *
from DemoCodes.Cartoon.Gentleman import *

# http://www.xeall.com/ribenmanhua/
url = "http://www.xeall.com/shenshi"

# enter your path
save_path = "Comic"

gentleman = Gentleman(url, save_path)
gentleman.hentai()




