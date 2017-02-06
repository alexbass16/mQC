#!/usr/bin/python
# -*- coding: utf-8 -*-
a = float(input())
b = float(input())
o = raw_input()
if o == 'mod':
    if b == 0:
        print('Деление на 0!')
    else:
        s = a % b
        print(s)
elif o =='-':
    print(a-b)
elif o =='+':
    print(a+b)
elif o =='*':
    print(a*b)
elif o =='pow':
    print(a**b)
elif o =='/':
    if b == 0:
        print('Деление на 0!')
    else:
        s = a / b
        print(s)
elif o =='div':
    if b == 0:
        print('Деление на 0!')
    else:
        s = a // b
        print(s)
else:
    print('please, enter correct operation!')