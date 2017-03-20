#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys



# 扫描域名策略
# 1 = 和域名全称相关: 包含 job.wooyun.org
# 2 = 和主域名相关: 包含 wooyun.org
# 3 = 和域名的名字相关: 包含 wooyun
basedomain = 1

# 判断文件或目录存在的状态码，多个以逗号隔开
# exclude_status = [200,403]
exclude_status = [200]

# 预设默认扩展名
custom_extion = 'php'  # 自定义扩展名
default_extion = sys.argv[2] if len(sys.argv) == 3 else custom_extion


