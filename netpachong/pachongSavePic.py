#!/usr/bin/python3
# coding=utf-8
import os
import urllib.request
import re


class SavePic:
    def __init__(self, url, path):
        self.url = url
        self.path = path

    def create_save_path(self, path):
        if not os.path.exists(path):
            print("create: %s" % path)
            os.mkdir(path)
        else:
            print("path: %s exists" % path)

    def save_picture(self, url, path):
        request = urllib.request.Request(url)
        request.add_header('User-Agent',
                           'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
        request.add_header('GET', url)

        print("save pic: %s" % url)
        try:
            response = urllib.request.urlopen(request, timeout=180)
            data = response.read()
            file = open(path, 'wb')
            file.write(data)
            file.close()
            print("==>finished.")
        except Exception as e:
            print("==>failed. Error: %s" % str(e))
            return None
