#!/usr/bin/python3
# coding=utf-8

import re

from netpachong.pachongBase import *
from netpachong.pachongSavePic import *


class Cartoon:
    def __init__(self, url, path):

        self.base_url = "http://www.xeall.com/shenshi"
        self.url = url
        self.path = path
        self.content = Base(url).get_content(self.url)
        if self.content:
            pass
        else:
            print("open url: %s, Failed" % url)
        self.title = self.get_cartoon_title(self.content)
        self.cartoon_page_list = self.get_cartoon_pages(self.content)
        self.check_pic_exists = False

    # 获取漫画页面的title
    def get_cartoon_title(self, content):
        splite_rule = re.compile(r'name="keywords" content="(.*?)".*?/>', re.S)
        result = re.findall(splite_rule, content)
        title = result[0]
        if re.search(r'[\/|\||\\|\*|\"|\>|\<|\?|\:]', title):
            print("title including illegal character, change")
            title = re.sub(r'[\/|\||\\|\*|\"|\>|\<|\?|\:]', '_', title, 0)
        print("title：%s" % title)
        return title

    # 获取漫画页面的picture
    def get_cartoon_pages(self, content):
        splite_rule = re.compile(r'class="pagelist">(.*?)</ul>', re.S)
        result = re.search(splite_rule, content)
        cartoon_page_list = result.groups(1)

        splite_rule = re.compile(r'href=\'(.*?)\'>.*?</li>')
        items = re.findall(splite_rule, cartoon_page_list[0])

        items.pop(0)
        items.pop(0)
        items.pop(len(items) - 1)

        cartoon_page_array = []
        cartoon_page_array.append(self.url)
        for item in items:
            cartoon_page = self.base_url + '/' + item
            cartoon_page_array.append(cartoon_page)
        print("漫画所有页面获取完成：%s" % cartoon_page_array)
        return cartoon_page_array

    def get_cartoon_pic(self, cartoon_page_url):
        pic_content = Base(cartoon_page_url).get_content(cartoon_page_url)

        splite_rule = re.compile(r'<img alt=".*?src="(.*?)".*?/>', re.S)
        result = re.search(splite_rule, pic_content)
        picture = result.groups(1)[0]
        if re.search(r'\ ', picture):
            print('including illegal character, change it')
            picture = re.sub(r'\ ', '%20', picture, 0)
        return picture

    def savepic(self):
        pic_save = SavePic(self.cartoon_page_list, self.path)
        pic_save.create_save_path(self.path)
        save_path = self.path + '/' + self.title
        pic_save.create_save_path(save_path)
        if len(os.listdir(save_path)) >= len(self.cartoon_page_list):
            print(self.title, " has been downloaded")
            return
        print("获取漫画图片")
        if len(os.listdir(save_path)) >= (len(self.cartoon_page_list) / 2):
            print("前次未完全下载, 检查图片是否存在")
            self.check_pic_exists = True
        for i in range(0, len(self.cartoon_page_list) - 1):
            pic_file = save_path + '/' + str(i + 1) + '.jpg'
            pic_url = self.get_cartoon_pic(self.cartoon_page_list[i])
            if self.check_pic_exists:
                if os.path.exists(pic_file):
                    print(pic_file, " already exists")
                    continue
            pic_save.save_picture(pic_url, pic_file)
