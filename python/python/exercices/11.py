# -*-coding:UTF-8 -*
import math
import easygui

def isPrimer(n):
    print ("test")
    
def exercice_11():
    myList = [1,4,12,43,12,44]
    monChoix = easygui.integerbox()
    for i in myList:
        if monChoix == i:
            break
    else:
        easygui.msgbox("the number doesn't exist on my list")
        print ("test")

def exercice_11_2 ():
    monChoix = easygui.integerbox("Enter a positive number. I'll tell is it's a primer one :", "", 7, 1)
    div = monChoix - 1
    while div > 2:
        print("{} % {} = {}".format(monChoix,div,monChoix%div))
        if (monChoix % div == 0):
            easygui.msgbox("not primer and first divider is {}".format(div))
            break
        div -= 1
    else:
        easygui.msgbox("your number {} is primer, congrats ! ".format(monChoix))
        
exercice_11_2()        