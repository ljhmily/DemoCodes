#!/usr/bin/python3
# coding=utf-8
import json
import urllib.request
from urllib import parse

import simplejson as simplejson


def request(url, headers, *args):
    if args:
        request = urllib.request.Request(url=url, headers=headers, data=args[0])
    else:
        request = urllib.request.Request(url=url, headers=headers)
    try:
        response = urllib.request.urlopen(request, timeout=60)
    except Exception as e:
        print(str(e))
    return response.read().decode('utf-8')


def get_token(url, headers):
    content = request(url, headers)
    # token = eval(response)["access_token"]
    token = json.loads(content)
    return token["access_token"]


def main(url, headers):
    tokenurl = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % get_token(url, headers)
    content = {
        "touser": "Midea_liuhao",
        "toparty": "9",
        "totag": "",
        "msgtype": "text",
        "agentid": 7,
        "text": {
            "content": "Test title " + "\n" + "Holiday Request For Pony(http://xxxxx)"
        },
        "safe": 0
    }
    data = json.dumps(content).encode('utf-8')
    response = request(tokenurl, headers, data)
    print(response)


if __name__ == '__main__':
    wxid = 'wxf2d0fbaa5692b4ef'
    wxsecret = '3_8IVdFrudMu6Y4kqEaBAqOVuCDn_2vj8IPeGRpJRQwg7i85aI2EvSehaMzCQ6ht'
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    headers = {'User-Agent': user_agent}
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (wxid, wxsecret)
    main(url, headers)
