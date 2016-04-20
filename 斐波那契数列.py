#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      公子小超
#
# Created:     20/04/2016
# Copyright:   (c) 公子小超 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#feibo naqi shulie 1

"""def f(x):
    if x<2:
        return x
    else:
        return (f(x-1)+f(x-2))"""


#feibo naqi shulie 2
def f(x):
    t=[1,1]
    i=2
    while i<=x:
        t.append(t[i-1]+t[i-2])
        i+=1
    return t[x]