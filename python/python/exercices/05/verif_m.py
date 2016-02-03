 
# -*- coding: utf-8 -*-
"""Module de vérification."""
# fichier : verif_m.py
# auteur : Bob Cordeau

# imports
from sys import exit


# Classe d'erreur.
class VerifError(Exception) :
    "Exception de vérification."
    def __init__(self,msg,entree,reference) :
        self.msg = msg
        self.entree = entree
        self.reference = reference
    def __str__(self) :
        return self.msg

# fonctions
def verif(entree, reference, precision=0, comment=""):
    """Vérifie que le numérique d'entrée est égal à la référence,
    à la précision près.
    """
    print("{}[{}, {}]".format(comment, entree, reference), end=" ")
    if abs(entree - reference) <= precision:
        print(": ok")
    else:
        print("### ko ! ###")

def verifSeq(entree, reference, comment=""):
    """Vérifie que la séquence d'entrée est égal à la référence."""
    print("{}[{}..., {}...]".format(comment, entree[:3], reference[:3]), end=" ")
    ok = len(entree) == len(reference)
    if ok :
        for i, j in enumerate(entree):
            ok = ok and (j == reference[i])
            if not ok : break
    if ok:
        print("ok")
    else:
        print("### ko ! ###")


# Auto-test ---------------------------------------------------------
if __name__=='__main__':
    verif(abs(-6/2), 3, comment="Teste la fonction 'abs' : ")
    pi = 3.142
    print("\npi = {}".format(pi))
    # Ok
    verif(pi, 3.14, 1e-2, comment="à 1e-2 : ")
    # Erreur
    verif(pi, 3.14, 1e-3, comment="à  1e-3 : ") 


    print("\nVérification d'une liste :")
    # Ok
    verifSeq("abcd", "abcd", comment="séquences identiques:")
    verifSeq([], [], comment="séquences (vides) identiques:")
    # Erreur
    verifSeq("abcd", "abcdef", comment="séquences de longueur différente:")
    verifSeq("abcd", "defg", comment="séquences de contenu différent:")