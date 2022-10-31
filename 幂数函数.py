
ans=[88421,122,48,2244,4,142242,248,122]
for i in ans:
    temp=0
    while i:
        temp+=i%10
        i//=10
    temp=ord('A')+temp-1
    print(chr(temp),end='')
