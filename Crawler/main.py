#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Marioo'
import queue
import threading
from urllib.parse import urlparse
from Crawler.quchong import urlFilter
from Crawler.download import *
from libs.common import *

lr = queue.Queue()


class Crawler(object):
    def __init__(self, url):
        super(Crawler, self).__init__()
        self.url = url
        self.queue = queue
        self.basedomain = get_basedomain(url)

    class WyWorker(threading.Thread):
        def __init__(self, lr):
            threading.Thread.__init__(self)
            self.lr = lr

        def run(self):
            while True:
                # 用no_timeout读取Queue队列，直接异常退出线程避免阻塞
                try:
                    thread_url =lr.get_nowait()
                    # print(thread_url)
                    print("Start crawling "+thread_url)
                    page_url = Get_links(url=thread_url)
                    # print(page_url)
                    resources.extend(page_url)
                except Exception as e:
                    break

    def craw(self):
        lr.put(self.url)
        global resources
        resources = []
        g_existURL = []
        g_subdomainUrl = []
        g_existURL.append(self.url)
        while not lr.empty():
            threads = []  # 初始化线程组
            for i in range(32):
                threads.append(self.WyWorker(lr))
            for t in threads:  # 启动线程
                t.start()
            for t in threads:  # 等待线程执行结束后，回到主线程中
                t.join()
            page_url = urlFilter(resources)
            for i in page_url:
                netloc = urlparse(i).netloc
                # print(netloc)
                if self.basedomain == netloc:    # 域名处理
                    if i not in g_existURL:
                        g_existURL.append(i)
                        lr.put(i)
                else:
                    i_subdomainUrl = get_basedomain(i)
                    if i_subdomainUrl not in g_subdomainUrl:
                        g_subdomainUrl.append(i)
        return sorted(g_existURL)

