#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Marioo'
import queue
from libs.FileUtils import FileUtils
queue = queue.Queue()

# 全局配置
using_dic = '/dics/dirs.txt'  # 使用的字典文件
threads_count = 1  # 线程数
timeout = 3  # 超时时间
allow_redirects = True  # 是否允许URL重定向
headers = {  # HTTP 头设置
             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
             'Referer': 'http://www.google.com',
             'Cookie': 'whoami=wyscan_dirfuzz',
             }
proxies = {  # 代理配置
    # "http": "http://user:pass@10.10.1.10:3128/",
    # "https": "http://10.10.1.10:1080",
    # "http": "http://127.0.0.1:8118", # TOR 洋葱路由器
}


# class DIR_Fuzz(object):
#     def __init__(self, siteurl):
#         super(DIR_Fuzz).__init__()
#         self.siteurl = siteurl
#
#     def fuzz_start(self):
#
#         if not self.siteurl.startswith('http://'):
#             siteurl = 'http://%s' % self.siteurl
#
#         global dir_exists
#         dir_exists = []
#
#         for line in FileUtils.getLines(using_dic):
#             line = '%s/%s' % (siteurl.rstrip('/'), line.replace('%EXT%', file_ext))
#             queue.put(line)


for line in FileUtils.getLines(using_dic):
    line = '%s/%s' % (siteurl.rstrip('/'), line.replace('%EXT%', file_ext))
    queue.put(line)