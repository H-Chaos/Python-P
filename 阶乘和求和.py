#-------------------------------------------------------------------------------
# Name:        濠碘槅鍨埀顒冩珪閸?
# Purpose:
#
# Author:      闂佺娴氶崜娆撴偤濞嗘垳鐒婇煫鍥ㄦ皑瀛?
#
# Created:     20/04/2016
# Copyright:   (c) 闂佺娴氶崜娆撴偤濞嗘垳鐒婇煫鍥ㄦ皑瀛?2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#jiecheng 1
g=int(input("Please input the Sum what you want to calculate:"))
s=0
for x in range(1,g+1):          #huozhe range(g)
    s+=x                        #s+=(x+1)
    g-=1
print(s)


#jiecheng 2

def f(x):
    if x<=1:
        return 1
    else:
        return x*f(x-1)

#jiecheng 3
from functools import reduce
g=int(input('nixiangjisuan de zhi:'))
print(reduce(lambda x,y:x*y,range(1,g+1)))

#qiuhe 1
g=int(input("Please input the Sum what you want to calculate:"))
s=0
for x in range(1,g+1):
    s+=x
    g-=1
print(s)

#qiuhe 2
from functools import reduce
g=int(input('nixiangjisuandezhi:'))
print(reduce(lambda x,y:x+y,range(g+1)))