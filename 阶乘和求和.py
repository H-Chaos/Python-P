#-------------------------------------------------------------------------------
# Name:        婵☆垪鈧櫕鍋?
# Purpose:
#
# Author:      闁稿浚鍓欓悺娆戜焊韫囨氨孝
#
# Created:     20/04/2016
# Copyright:   (c) 闁稿浚鍓欓悺娆戜焊韫囨氨孝 2016
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
print(reduce(lambda x,y:x*y,range(1,g)))

#qiuhe 1
g=int(input("Please input the Sum what you want to calculate:"))
s=0
for x in range(1,g+1):
    s+=x
    g-=1
print(s)
