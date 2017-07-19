#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:wanga 
@file: main.py 
@time: 2017/07/13 
"""
file = open("data.txt", "r")
data = ""

for line in file:
    data += line

data = data.replace("&&", "\n")
data = data.replace("==", "=")

equations = data.split("\n")
equations = sorted(equations, key=lambda v: len(v))

# for equ in equations:
#     print(equ)

new_equs1 = []
for equ in equations:
    front, back = equ.split("=")
    move = '-'+back+"+"+front+"=0"
    #print(move)
    new_equs1.append(move)

new_equ2 = []
for equ in new_equs1:
    equ = equ.replace("--", "+")
    new_equ2.append(equ)


dist = open("result.py", "w")
dist.writelines("a = [1]*%d\n" % len(new_equ2))
for index, equ in enumerate(new_equ2):
    trans = equ.replace("=0", "")
    if trans.find("+a[%d]" % index) != -1:
        move = trans.replace("+a[%d]" % index, "")
        dist.writelines("a[%d]=-(%s)\n" % (index, move))
    else:
        move = trans.replace("-a[%d]" % index, "")
        dist.writelines("a[%d]=%s\n" % (index, move))

dist.writelines("for v in a:\n")
dist.writelines("   print(chr(v), end=\'\')\n")
