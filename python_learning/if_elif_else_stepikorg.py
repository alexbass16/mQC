#!/usr/bin/python
# -*- coding: utf-8 -*-

recommend = int(input('need: '))
oversleep = int(input('oversleep: '))
ann = int(input('you: '))
if ann >= recommend and ann <= oversleep:
    print "Good for you"
elif ann < recommend:
    print "You need a rest!"
elif ann > oversleep:
    print "Wake up earlier, please!"
