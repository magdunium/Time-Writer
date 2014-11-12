#coding: utf-8

import time

file = open("time.txt", "a+") #tu jest file, ale mogłoby być coś innego

file.write(time.asctime() + "\n" )

file.close()

#execfile("test.py") #wywołuj forlater

