# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 15:45:45 2020

@author: Admin
"""

import random
n=int(input("n="))
list1=[]
i=1 
while i<=n:
    a=random.random()
    list1.append(a)
    i+=1
print(list1)
max=list1[0]
i=1
while i<n:
    if max<list1[i]:
        max=list1[i]
    i+=1
print("giá trị lớn nhất là:",max)
print("kết thúc chương trình")