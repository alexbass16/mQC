#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Проверка на счастливый билет"""
a = raw_input()
b = int(a[0]) + int(a[1]) + int(a[2])
c = int(a[3]) + int(a[4]) + int(a[5])
if b == c:
    print("Счастливый")
else:
    print("Обычный")