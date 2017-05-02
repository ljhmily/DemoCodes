import re
import urllib
import urllib.request

from collections import deque

queue = deque()
visited = set()

# url = 'http://news.dbanotes.net'
url = 'http://www.baidu.com'

queue.append(url)
count = 0


def saveFile(data, serial):
    savePath = "网络爬虫 v1.1 alpha/tmp_%s.log" % serial
    f_obj = open(savePath, 'wb')
    f_obj.write(data)
    #f_obj.close()


while queue:
    url = queue.popleft()
    visited |= {url}
    print("已抓取: " + str(count) + '正在抓取 << ' + url)
    count += 1
    try:
        urlopen = urllib.request.urlopen(url, timeout=3)
        if 'html' not in urlopen.getheader('Content-Type'):
            continue
        #olddata = urlopen.read()
        data = urlopen.read().decode('utf-8')
    except:
        continue

    saveFile(data.encode('utf-8'), count)

    linkre = re.compile('href=\"(.+?)\"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print("加入队列 >> " + x)
