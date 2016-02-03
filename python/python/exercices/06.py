# -*-coding:UTF-8 -*
import math
import easygui

def exercice_06():
    maChaine = "bonjour skander"
    maListe = ["bonjour", "skander", "your rock!"]
    print(" Exemple 1 ".center(40, '-'))
    for e in maChaine:
        print e
    print(" Exemple 2 ".center(40, '-'))
    for l in maListe:
        print l
    print("\n\n{:-^40}".format(" idem avec format "))
        
def exercice_07():
    for i in range (15):
        if i % 3 == 0:
            print i

def exercice_08():
    for i in range (10):
        print i
        if i == 5 :
            break

def exercice_09():
    for i in range (10):
        if i == 5 :
            continue
        print i            

def exercice_10():
    for x in range (-3,3):
        try :
            print math.sin(x)/x
        except ZeroDivisionError:
            print "dev per 0"

def exercice_11():
    myList = [1,4,12,43,12,44]
    monChoix = easygui.integerbox()
    for i in myList:
        if monChoix == i:
            break
    else:
        easygui.msgbox("the number doesn't exist on my list")
        print ("test")

exercice_11()