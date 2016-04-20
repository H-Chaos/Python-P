#-------------------------------------------------------------------------------
# Name:        濡€虫健1
# Purpose:
#
# Author:      閸忣剙鐡欑亸蹇氱Т
#
# Created:     20/04/2016
# Copyright:   (c) 閸忣剙鐡欑亸蹇氱Т 2016
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

#qiuhe 1
g=int(input("Please input the Sum what you want to calculate:"))
s=0
for x in range(1,g+1):
    s+=x
    g-=1
print(s)
