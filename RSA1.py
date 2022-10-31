#!/usr/bin/python
#coding:utf-8

import gmpy2
from Crypto.Util.number import long_to_bytes

N = 2175688405733541703870452086626738401792220260185622845647
e = 0x10001
c = 909189959980475048848571460773306576585339198658788147448
p1 = 12174597259764339563
p2 = 12211006709935453691
p3 = 14634929140319987959

r = (p1 - 1) * (p2 - 1) * (p3 - 1)
d = gmpy2.invert(e,r)
n = pow(c,d,N)

print (long_to_bytes(n))


