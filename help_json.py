# coding: utf-8

'''
JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式。
它基于JavaScript（Standard ECMA-262 3rd Edition - December 1999）的一个子集。 
JSON采用完全独立于语言的文本格式，但是也使用了类似于C语言家族的习惯（包括C, C++, C#, Java, JavaScript, Perl, Python等）。
这些特性使JSON成为理想的数据交换语言。易于人阅读和编写，同时也易于机器解析和生成。

    编码：把一个Python对象编码转换成Json字符串   json.dumps()
        排序：json.dumps(data,sort_keys=True)
        缩进：json.dumps(data,indent=4)
        压缩：json.dumps(data, separators = (',', ':'))

    解码：把Json格式字符串解码转换成Python对象   json.loads()
   
'''

import requests
import json

def get_reponse(url):
    response = requests.get(url)
    dic = json.loads(response.text)
    dd = dic['dataList']
    # print(dd[0])
    L = []  # 存放所有的信息
    for d in dd:
        usr_dic = {}    # 存放单条需要的信息
        for k,v in d.items():
            if k =='avatarUrl':
                usr_dic['url'] = v  # 重新设置key名
            if k == 'darenNick':
                usr_dic['name'] = v
            if k == 'desc':
                usr_dic['desc'] = v

        L.append(usr_dic)

    print(len(L))
    print(L)

url = "https://mm.taobao.com/alive/list.do?scene=all&page=3"
get_reponse(url)