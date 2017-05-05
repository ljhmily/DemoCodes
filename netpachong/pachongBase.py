#!/usr/bin/python3
# coding=utf-8

import urllib.request
import zlib


class Base:
    def __init__(self, url):
        self.base_url = url
        self.url = self.base_url
        # 解析url内容
        self.content = self.get_content(self.base_url)

    def get_content(self, url):
        user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        headers = {'User-Agent': user_agent}
        try:
            request = urllib.request.Request(url, headers=headers)
            response = urllib.request.urlopen(request, timeout=60)
            if response.info().get('Content-Encoding') == 'gzip':
                content = zlib.decompress(response.read(), 16 + zlib.MAX_WBITS).decode('gb2312', 'ignore')
            else:
                content = response.read().decode('gb2312', 'ignore')
            return content
        except:
            return None
