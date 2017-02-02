#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы A часов в сутки, но пересыпать тоже вредно и не
стоит спать более B часов. Сейчас Аня спит H часов в сутки. Если режим сна Ани удовлетворяет рекомендациям передачи
“Здоровье”, выведите “Это нормально”. Если Аня спит менее A часов, выведите “Недосып”, если же более B часов, то
выведите “Пересып”.
Получаемое число A всегда меньше либо равно B.
На вход программе в три строки подаются переменные в следующем порядке: A, B, H. """


recommend = int(input('need: '))
oversleep = int(input('oversleep: '))
ann = int(input('you: '))
if ann >= recommend and ann <= oversleep:
    print "Good for you"
elif ann < recommend:
    print "You need a rest!"
elif ann > oversleep:
    print "Wake up earlier, please!"
