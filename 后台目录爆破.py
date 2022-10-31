# -*- coding:utf-8 -*-
# 运行环境为python3.0   作者：Screw

import requests
url=input("输入你的url  :")
script=int(input("选择脚本1.asp 2.php 3.jsp 4.sapx  :"))
true_script=""
ture_url=""
if script==1:
    true_script="ASP.txt"
elif script==2:
    true_script="PHP.txt"
elif script==3:
    true_script="JSP.txt"
elif script==4:
    true_script="ASPX.txt"
else :
    print("输入错误！")
def baopo():
    print(u"                                 爆破开始耐心等待：")
    str=open(true_script).read()
    str_list=str.split('\n')
    for i in str_list:
        # print (url)
        url_true=url+i

        try:
            a=requests.get(url_true).status_code
            if a>=200 and a<=300:
                print(url_true)
        except:
            pass
    print(u"爆破结束！")