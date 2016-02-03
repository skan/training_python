# -*-coding:UTF-8 -*
import os

class MaPersonne:
    """ Ma première classe,
    elle évoluera au fur et à mesure de l'apprentissage """
    nombrePersonne = 0
    def __init__(self, age):
        print("constructeur de ma première classe")
        self.nom = "hamza"
        self.ville = "tunis"
        self.age = age
        MaPersonne.nombrePersonne += 1

class tableauNoir:
    superficie = 0
    nombreTableau = 0
    def __init__(self):
        self.superficie = ""
        tableauNoir.nombreTableau += 1
    def ecrire (self, message_a_ecrire):
        if (self.superficie != ""):
            self.superficie += "\n"
        self.superficie += message_a_ecrire
    def lire (self):
        if (self.superficie == ""):
            return "le tableau est vide"
        else:
            return self.superficie
    def effacer (self):
        self.superficie = ""
    def combien (cls):
        print("jusqu a present {} tableau crees".format(cls.nombreTableau))
    combien = classmethod (combien)  # Fonction built-in de Python pour faire comprendre qu'il s'agit d'une méthode de classe, pas d'une méthode d'instance.

print ("j'apprends pyton")

skander = MaPersonne(35)
walid  = MaPersonne(40)
print(skander.nom)
print(skander.ville)
skander.ville = "mahdia"
print(skander.ville)
print(skander.age)
print(walid.age)
print(walid.nombrePersonne)
print(skander)
print ("****************")
print ("comprendre l utilisation de self")
tableau = tableauNoir()
tableauTest = tableauNoir()
tableau.ecrire("tests")
print(tableau.lire())
print(tableau.superficie)
tableauNoir.ecrire(tableau, "test de self")
print(tableau.superficie)
tableau.effacer()
print(tableau.lire())
tableau.ecrire("ecire de nouveau")
print(tableau.lire())
tableauNoir.combien()
os.system("pause")

