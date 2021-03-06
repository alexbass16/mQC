#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Требуется определить, является ли данный год високосным.
Напомним, что високосными годами считаются те годы, порядковый номер которых либо кратен 4, но при этом не кратен 100,
либо кратен 400 (например, 2000-й год являлся високосным, а 2100-й будет невисокосным годом).
Программа должна корректно работать на числах 1900≤n≤3000.
Выведите "Високосный" в случае, если считанный год является високосным и "Обычный" в обратном случае

"""

year = int(input("Enter year for testing, please: "))
if year > 3000 or year < 1900:
    print "wrong format"
else:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print "Высокосный"
    else:
        print "Обычный"