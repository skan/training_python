import os
from random import randrange
import data

nameList = ["Maison",
            "Dessert",
            "Jouet",
            "Chocolat",
            "Skander",
            "Voiture",
            ]
nombreMots = len(nameList)

def getWord(nombreMot):
    tirage = randrange(nombreMot)
    print (tirage)
    

# test de la fonction table
if __name__ == "__main__":
    print ("hello")
    getWord(4)
    os.system("pause") 