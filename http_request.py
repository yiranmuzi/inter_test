# -*- coding:utf-8 -*-
# @Time    : 2020/7/3 18:19
# @Author  : muzijie
# @File    : http_request.py

import requests

def http_request(url,data,token=None,method='post'):
    header={'X-Lemonban-Media-Type':'lemonban.v2','Authorization':token}
    if method=='get':
        result=requests.get(url,json=data,headers=header)
    else:
        result = requests.post(url,json=data,headers=header)
    return result.json()