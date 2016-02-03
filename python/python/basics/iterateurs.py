#-*- coding: utf-8 -*-
import os

# une liste est un itérateurs
#liste = [1,2,3,4,5,6,7,8,9,10]

# Créer une classe itérateur
class MonIter():

    current=0
    
    def __init__(self,stop):
        self.stop=stop

    def __iter__(self) :
        return self

    def next(self) :
        self.current+= 1     
        if self.current>self.stop:
            raise StopIteration
        if self.current == 5:
            print ("Quoi déjà 5eme tour?")
        return self.current   
   
# main

tempVar = MonIter(10)
tempDir = dir (tempVar)
print (tempDir)
for i in MonIter(10):
    print (i)

#for x in liste:
#   print (x)
    
os.system("pause")