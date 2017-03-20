#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append("../")
from urllib.parse import urlparse
from libs.tldextract import extract
from libs.config import *


class UrlSplitParser(object):
    """docstring for UrlSplitParser
	   碎片化信息处理并集，生成其因变量组 [dependents]
	"""

    def __init__(self, urlobj, extion=default_extion):
        super(UrlSplitParser, self).__init__()
        o = urlparse(urlobj)
        self.url = o.geturl()
        # print(self.url)
        self.scheme = o.scheme  # scheme='http', netloc='www.baidu.com', path='/index.php', params='',
        # print(self.scheme)
        self.netloc = o.netloc
        # print(self.netloc)
        self.path = o.path
        # print(self.path)
        self.paths = self.split_path()  # 切割路径,将路径切割存放起来.
        # print(self.paths)
        self.query = o.query  # query='username=guol'
        self.fragment = o.fragment
        self.domain = extract(o.netloc).domain
        # print(self.domain)
        self.rootdomain = extract(o.netloc).registered_domain
        # print(self.rootdomain)
        self.subdomain = extract(o.netloc).subdomain.split('.')
        # print(self.subdomain)
        self.domain_info = self.get_domain_info()
        # print(self.domain_info)
        self.extion = extion
        # print(self.extion)
        self.file_ext = self.get_extion()
        # print(self.file_ext)
        self.urlfile = self.get_urlfile()
        # print(self.urlfile)
        self.baseurl = self.scheme + '://' + self.netloc
        # print(self.baseurl)
        self.dependent = self.get_dependent()
        # print(self.dependent)

    def parse(self):
        urlsplit = {}
        # urlsplit['url'] = self.url
        urlsplit['scheme'] = self.scheme
        urlsplit['netloc'] = self.netloc
        urlsplit['query'] = self.split_query()
        urlsplit['path'] = self.split_path()
        urlsplit['extion'] = self.get_extion()
        urlsplit['fragment'] = self.fragment
        return urlsplit

    def split_query(self):
        query = {}
        condition = self.query.split('&')
        if len(condition) >= 1:
            for line in condition:
                line_split = line.split('=')
                if len(line_split) > 1:
                    query[line_split[0]] = line_split[1]
                else:
                    query[line_split[0]] = ''
            return query
        else:
            return ''

    def split_path(self):
        path = []
        for dirs in self.path.split('/'):
            if dirs != '': path.append(dirs)
        return path

    def split_fragment(self):
        fragment = []
        for frags in self.fragment.split('='):
            if frags != '':
                fragment.append(frags)
        return fragment

    def get_domain_info(self):
        # 扩充域名信息节点
        domain = self.domain
        subdomain = self.subdomain
        subdomain.append(domain)
        if '' in subdomain:
            subdomain.remove('')
        return subdomain

    def get_dependent(self):
        # 生成其因变量组
        dependent = []
        dependent.extend(self.split_query().keys())
        dependent.extend(self.split_query().values())
        dependent.extend(self.split_fragment())
        dependent.extend(self.get_paths()['path'])
        dependent.extend(self.domain_info)
        dependent.append(self.file_ext)
        dependent = list(set(dependent))
        if '' in dependent: dependent.remove('')
        return dependent

    def get_extion(self):  # 获取拓展名
        path = self.split_path()

        if len(path) >= 1:
            filename = path[-1].split('.')
            # print (filename)
            if len(filename) > 1:
                return filename[-1]
            else:
                return self.extion
        else:
            return self.extion

    def get_urlfile(self):
        # 初始化脚本文件
        urlfile = self.path
        if self.get_extion():
            file_ext = self.get_extion()
            if urlfile == '/':
                urlfile = urlfile + 'index.' + file_ext
            elif urlfile == '':
                urlfile = urlfile + '/index.' + file_ext
            elif not urlfile.endswith(file_ext):
                urlfile = urlfile + '.' + file_ext
        return urlfile

    def get_paths(self):
        paths = []
        segments = ['/']
        fullpath = ''
        if self.path.endswith('/'):
            for pathline in self.paths:
                paths.append(pathline)
                fullpath += '/' + pathline
                segments.append(fullpath)
        else:
            for pathline in self.paths:
                if pathline == self.paths[-1]:
                    if '.' in pathline:  # 最后一个是文件，判断是否存在扩展名
                        rstrip_path = pathline.replace(('.' + self.file_ext), '')
                        paths.append(rstrip_path)
                    else:
                        paths.append(pathline)
                else:
                    paths.append(pathline)
                    fullpath += '/' + pathline
                    segments.append(fullpath)

        return {'segment': segments, 'path': paths}
