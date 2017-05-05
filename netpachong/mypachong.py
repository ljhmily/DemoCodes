#!/usr/bin/python3
# coding=utf-8

import io
import os
import sys

import zlib

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import urllib.request
import re


class Comics:
    def __init__(self, url):
        self.base_url = url
        self.url = self.base_url
        self.path = "temp"
        # 解析url内容
        content = self.get_content(self.base_url)
        # 获取url的子页面列表
        self.page_list = self.get_page_list(content)
        # 获取子页面的漫画列表
        self.cartoon_list = self.get_cartoon_list(content)
        # 获取漫画页面的title、漫画的分页列表
        for cartoon_url in self.cartoon_list:
            self.title = self.get_cartoon_title(cartoon_url)
            self.cartoon_page_list = self.get_cartoon_pages(cartoon_url)
            self.save()

    def get_content(self, url):
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
        headers = {'User-Agent': user_agent}
        try:
            request = urllib.request.Request(url, headers=headers)
            response = urllib.request.urlopen(request, timeout=60)
            if response.info().get('Content-Encoding') == 'gzip':
                content = zlib.decompress(response.read(), 16 + zlib.MAX_WBITS).decode('gb2312', 'ignore')
            else:
                content = response.read().decode('gb2312', 'ignore')
            print("open url: %s, Success" % url)
            return content
        except Exception as e:
            print("open url: %s, Failed" % url)
            return None

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
        print("URL页面列表：%s" % page_array)
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
        print("漫画列表：%s" % cartoon_array)
        return cartoon_array

    # 获取漫画页面的title
    def get_cartoon_title(self, cartoon_url):
        cartoon_content = self.get_content(cartoon_url)

        splite_rule = re.compile(r'name="keywords" content="(.*?)".*?/>', re.S)
        result = re.findall(splite_rule, cartoon_content)
        # print(result[0])
        title = result[0]
        print("漫画标题：%s" % title)
        return title

    # 获取漫画页面的picture
    def get_cartoon_pages(self, cartoon_url):
        cartoon_content = self.get_content(cartoon_url)

        splite_rule = re.compile(r'class="pagelist">(.*?)</ul>', re.S)
        result = re.search(splite_rule, cartoon_content)
        cartoon_page_list = result.groups(1)

        splite_rule = re.compile(r'href=\'(.*?)\'>.*?</li>')
        items = re.findall(splite_rule, cartoon_page_list[0])

        items.pop(0)
        items.pop(0)
        items.pop(len(items) - 1)

        cartoon_page_array = []
        cartoon_page_array.append(cartoon_url)
        for item in items:
            cartoon_page = self.base_url + '/' + item
            cartoon_page_array.append(cartoon_page)
        print("漫画内容页面列表：%s" % cartoon_page_array)
        return cartoon_page_array

    def get_cartoon_picture(self, cartoon_page_url):
        pic_content = self.get_content(cartoon_page_url)

        splite_rule = re.compile(r'<img alt=".*?src="(.*?)".*?/>', re.S)
        result = re.search(splite_rule, pic_content)
        print("漫画内容图片：", result.groups(1)[0])
        picture = result.groups(1)[0]
        return picture

    def save_picture(self, picture_url, path):
        request = urllib.request.Request(picture_url)
        request.add_header('User-Agent',
                           'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
        request.add_header('GET', picture_url)

        try:
            print("save picture：%s success" % picture_url)
            response = urllib.request.urlopen(request, timeout=180)
            data = response.read()

            file = open(path, 'wb')
            file.write(data)
            file.close()
        except Exception as e:
            print("save picture：%s failed" % picture_url)
            return None

    def create_save_path(self, path):
        if not os.path.exists(path):
            print("path %s not exists, create" % path)
            os.mkdir(path)
        else:
            print("path %s exists" % path)

    def save(self):
        self.create_save_path(self.path)
        save_path = self.path + '/' + self.title
        self.create_save_path(save_path)

        for i in range(0, len(self.cartoon_page_list) - 1):
            pic_path = save_path + '/' + str(i + 1) + '.jpg'
            print(pic_path)
            self.pic_url = self.get_cartoon_picture(self.cartoon_page_list[i])
            self.save_picture(self.pic_url, pic_path)


url = "http://www.xeall.com/shenshi"
cartoon = Comics(url)
