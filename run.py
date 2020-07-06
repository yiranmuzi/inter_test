# -*- coding:utf-8 -*-
# @Time    : 2020/7/3 19:18
# @Author  : muzijie
# @File    : run.py


from http_request import http_request
from rw_excel import read_data
from rw_excel import  write_data

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gb18030")

token=None #全局变量初始值
def run(file_name,sheet_name,c1,c2):
    global token  #声明全局变量
    #首先取出测试用例
    all_case=read_data(file_name,sheet_name)

    uri='http://120.78.128.25:8766'
    #先执行第一条登录
    # test_data=all_case[0]   #2列：login/recharge  4列 get/post 5列 接口地址 6列 data 7列 期望结果

    for i in range(0,len(all_case)):
        test_data=all_case[i]
        response=http_request(uri+test_data[4],eval(test_data[5]),token,test_data[3])
        if test_data[1]=='login':
            token='Bearer '+response['data']['token_info']['token']
        write_data(file_name,sheet_name,i+2,c1,str(response))
        print(response)
        # 判断测试用例是否通过

        actual={'code':response['code'],'msg':response['msg']}
        if eval(test_data[6])==actual:
            print('测试用例执行通过')
            write_data(file_name,sheet_name,c1,c2,'PASS')
        else:
            print('测试用例执行不通过')
            write_data(file_name, sheet_name, c1, c2, 'FAILD')



run('test_case.xlsx','recharge',8,9)
