from urllib import request
SIMILAR_SET = set() # hash表 用来
extList = ('jpg','jpeg','js','css','png','gif','xml','ico','swf')

def urlFarmat(url):
    if request.urlparse(url)[2] == '':
        url = url + '/'
    url_structure = request.urlparse(url)
    netloc = url_structure[1]
    net_path = url_structure[2]
    net_query = url_structure[4]
    temp = (netloc,tuple([len(i) for i in net_path.split('/')]),tuple(sorted(([i.split('=')[0] for i in net_query.split('&')]))))
    return temp

def url_similar_control(url):
    '''
    :URL 相似度控制
    :param url:
    :return: True url未重复； False url重复
    '''
    t = urlFarmat(url)
    if t not in SIMILAR_SET:
        SIMILAR_SET.add(t)
        return True
    return False

def urlFilter(all_url):
    '''
    :过滤图片，js，css
    :param all_url:
    :return: 返回过滤后的url
    '''
    __lis = []
    url_list = []
    for url in all_url:
        flag = url_similar_control(url.strip('\n'))
        if flag:
            __lis.append(url.strip('\n'))

    for url in __lis: #剔除文件
        path = request.urlparse(url)[2]
        ext = path.split('/')[-1].split('.')[-1]
        if ext not in extList:
            url_list.append(url)
    return url_list


