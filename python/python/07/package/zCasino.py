# -*-coding:Latin-1 -*
import os
from random import randrange
from math import ceil

#import pdb; pdb.set_trace()
# declare the initial amount
totalAmount = 1000

while totalAmount > 0:    
    # get the number to bet
    betNumber = -1
    while betNumber < 0 or betNumber > 49:
        betNumber = input("select a betNumber: ")     
        try:
            betNumber = int (betNumber)
        except ValueError:
            print ("please type a number")
            betNumber = -1
            continue
        if betNumber < 0 or betNumber > 49:
            print ("number must be in 0 .. 49 range")
    betAmount = -1
    while betAmount < 0 or betAmount > totalAmount:
        betAmount = input("Select the amount to deal: ") 
        try:
            betAmount = int (betAmount)
        except ValueError:
            print ("you didn't type a number ")
            continue
        if betAmount > totalAmount:
            print ("your don't have such an amount, your remaining money is " , totalAmount, "$")
            betAmount = -1
            
    print("your bet Number is " , betNumber)
    print("your bet Amount is ", betAmount)
    print("Goood Luck")
    
    tirage = randrange(50)
    
    print ("tirage result", tirage)
    if tirage == betNumber:
        gain = betAmount * 3
    elif betNumber%2 == betAmount%2:
        gain = ceil(betAmount / 2)
    else:
        gain =  betAmount * -1 
    totalAmount += gain
    
    print("your balance will be modified by" , gain, "$")
    print("your new balance is ", totalAmount, "$")
 
os.system("pause")