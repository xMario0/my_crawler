#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Marioo'
from Crawler.main import Crawler

if __name__ == '__main__':
    url = "http://www.waerfa.com/"
    Crawl = Crawler(url)
    a = Crawl.craw()
    for i in a:
        print(i)
        # netloc = urlparse(url).netloc
        # print(get_basedomain(url),netloc)
