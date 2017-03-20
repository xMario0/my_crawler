#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Marioo'
import subprocess
import json


def Get_links(url):

    cookie = ""
    auth = ""
    post = ""
    timeout = 10
    all_url = []
    p = subprocess.Popen(["/Users/Mario/Environment/phantomjs/bin/phantomjs Crawler/crawler.js {0} {1} {2} {3}".format(url,cookie, auth, post, timeout) ],shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        a = str(line, 'utf-8')
        if 'url' and 'method' in a:
            dictinfo = json.loads(a)  # 字符串格式化字典
            if 'http:' in dictinfo['url']:
                if dictinfo['url'] not in all_url:  # 简单去掉相同链接
                    all_url.append(dictinfo['url'])
                    # print(dictinfo['url'])
        else:
            pass

    return all_url
