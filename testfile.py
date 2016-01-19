# -*- coding:utf-8 -*-

def func(i):
    t = divmod(i,3)
    return t[1]

li = (1,5,3,2,9,19,24)
print(sorted(li))
# [1, 2, 3, 5, 9, 19, 24]
print(sorted(li,reverse=True))
# [24, 19, 9, 5, 3, 2, 1]
print(sorted(li,key=func))
# [3, 9, 24, 1, 19, 5, 2]
print(sorted(li,key=func,reverse=True))
# [5, 2, 1, 19, 3, 9, 24]
com