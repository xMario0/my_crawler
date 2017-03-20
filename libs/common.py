#!/usr/bin/env python
# -*- coding: utf-8 -*-


from libs.UrlSplitParser import *


def get_basedomain(url):
    try:
        if basedomain == 1:
            return urlparse(url).netloc
        elif basedomain == 2:
            return extract(url).registered_domain
        elif basedomain == 3:
            return extract(url).domain  # 更加有关联性的处理方法
    except Exception as e:
        pass




def get_segments(url):
    url_webdirs = []
    parser_obj = UrlSplitParser(urlparse(url))
    for segment in parser_obj.get_paths()['segment']:
        #print(segment) #链接所有的相对路径
        url_webdirs.append(parser_obj.baseurl + segment)
    return url_webdirs


def get_baseurl(link):
    netloc = urlparse(link).netloc
    if netloc:
        split_url = link.split(netloc)
        baseurl = '%s%s' % (split_url[0], netloc)
        return baseurl


