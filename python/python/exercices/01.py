# -*-coding:UTF-8 -*
import sys
from math import sqrt
#print (sys.version)

def exerice_01():
    time = 6.892
    dist = 19.7
    speed = dist/time
    print ("speed = {0:.2f}\n".format(speed))
    prenom = str(raw_input("prenom ?"))
    age = int(raw_input("age ?"))
    print ("{}\n nom: {} \t age:{}".format("-"*40,prenom,age))
    print (type(prenom))
    print (type(age))
    
 
def exercice_021():
    print "exercice 2"
    myFloat = float(raw_input("float ? "))
    if myFloat > 0:
        print ("racine de {} = {}".format(myFloat,sqrt(myFloat)))
    else:
        print ("error: negative float value")

def exercice_021():        
    mot1 = str(raw_input("mot1 : "))
    mot2 = str(raw_input("mot2 : "))
    
    if mot1 < mot2:
        print mot1
    else:
        print mot2
    
    res = mot1 if mot1 < mot2  else mot2  # intstruction ternaire
    print ("methode 2: {}".format(res))
        
def exercice_022():
    pSeuil = 2.3
    vSeuil = 7.41
    pression = float(input("pression : "))
    volume = float(input("volume : "))
    
    if pression > pSeuil and volume > vSeuil:
        print "STOP"
    elif pression > pSeuil :
        print ("increas volume")
    elif volume > vSeuil:
        print ("increas pressure")
    else:
        print("tout va bien")

def exercice_4():        
    a = 0
    b = 10
    for a in range(b):
        print a
    
    print ("{}".format("*"*10))
    
    while b > 0:
        if b % 2 == 1:
            print b
        b -= 1

def exercice_5():
    a = int(input ("saisir un entier de 1 a 10: "))
    while not 1 < a < 10:
        a = int(input ("saisir un entier de 1 a 10: "))

