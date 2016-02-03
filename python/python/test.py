#!/usr/bin/python2.7
#-*- coding: utf-8 -*-
def generateur(n):
   for i in range(n):
      if i == 5:
         print ("already at 5 !")
      yield i+1

i = generateur(10)
for v in i:
    print v
    