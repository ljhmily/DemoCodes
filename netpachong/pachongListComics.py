#!/usr/bin/python3
# coding=utf-8

import re

from netpachong.pachongBase import *
from netpachong.pachongGetPic import *


class Comics:
    def __init__(self, url, path):
        self.base_url = url
        self.url = self.base_url
        self.path = path
        # 解析url内容
        self.content = Base(self.url).content
        if self.content:
            print("open url: %s, Success" % url)
        else:
            print("open url: %s, Failed" % url)
        # 获取url的子页面列表
        self.page_list = self.get_page_list(self.content)
        # 获取子页面的漫画列表
        self.cartoon_list = self.get_cartoon_list(self.content)

    # 获取url的子页面列表
    def get_page_list(self, content):
        split_rule = re.compile(r'<select\ name=\'sldd\'.*?>(.*?)</select>', re.S)
        result = re.search(split_rule, content)
        # groups()	返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
        page_list = result.groups(1)

        split_rule = re.compile(r'value=\'(.*?)\'.*?</option>', re.S)
        items = re.findall(split_rule, page_list[0])

        page_array = []
        for item in items:
            page_url = self.base_url + '/' + item
            page_array.append(page_url)
        print("URL子页列表：%s" % page_array)
        return page_array

    # 获取子页面的漫画列表
    def get_cartoon_list(self, content):
        splite_rule = re.compile(r'class="piclist listcon">.*?>(.*?)</ul>', re.S)
        result = re.search(splite_rule, content)
        cartoon_list = result.groups(1)

        splite_rule = re.compile(r'<a href="/shenshi/(.*?)".*?</li>', re.S)
        items = re.findall(splite_rule, cartoon_list[0])

        cartoon_array = []
        for item in items:
            cartoon_url = self.base_url + '/' + item
            cartoon_array.append(cartoon_url)
        print("URL子页漫画列表：%s" % cartoon_array)
        return cartoon_array

    def main(self):
        for cartoon_url in self.cartoon_list:
            cartoon_urls = Cartoon(cartoon_url, self.path)
            cartoon_urls.savepic()
