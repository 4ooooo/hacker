import gmpy2
c=eval(input("请输入c"))
p=eval(input("请输入p"))
q=eval(input("请输入q"))
e=eval(input("请输入e"))
phi=(p-1)*(q-1)
d=gmpy2.invert(e,phi)
n=p*q
m=pow(c,d,n)
print(bytes.fromhex(hex(m)[2:]))

