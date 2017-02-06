#!/usr/bin/python
# -*- coding: utf-8 -*-
a=int(input())
b=int(input())
c=int(input())
if a>=b and a>=c:
    print(a)
else:
    if b>=a and b>=c:
        print(b)
    else:
        if c>=a and c>=b:
            print(c)
if a<=b and a<=c:
    print(a)
else:
    if b<=a and b<=c:
        print(b)
    else:
        if c<=a and c<=b:
            print(c)
if b<=a<=c or b>=a>=c:
    print(a)
else:
    if a<=b<=c or a>=b>=c:
        print(b)
    else:
        if a<=c<=b or a>=c>=b:
            print(c)