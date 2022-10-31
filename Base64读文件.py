base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
path = 'D:/CTF/BUU'   #读取文件的位置
def change(string_test) :
    strings_ans = ""
    for every in string_test :
        bin_num = ""
        if every == "=" :
            return strings_ans
        else :
            num = base64.find(every)
            while num != 0 :
                bin_num += str(num%2)
                num = int(num/2)
            while len(bin_num) <6 :
                bin_num += "0"
            bin_num = bin_num[::-1]
        strings_ans += bin_num
    return strings_ans
def answer(strings_last) :
    ans = ""
    strings_temp = change(strings_last)
    if strings_last.count('=') == 1 :
        ans += strings_temp[-2:]
    else :
        ans += strings_temp[-4:]
    return ans
with open(path + "/" + "base64.txt","r") as in_file :   #输入文件的名称
    strings_first = in_file.readlines()
    strings = []
    for every_strings in strings_first :
        if every_strings[-2] =="=" :
            strings.append(every_strings)
with open(path + "/" + "out.txt","w") as out_file :    #输出文件的名称
    ans = ""
    for line in strings :
        ans += answer(line)
    num = 0
    list_num = []
    for i in range(0,len(ans)) :
        num = num*2+int(ans[i])
        if (i+1)%8 == 0 :
            list_num.append(num)
            num = 0
    ans = ""
    for i in list_num :
        ans += chr(i)
    out_file.write(ans)

