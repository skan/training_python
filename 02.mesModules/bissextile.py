#/usr/bin/python
# -*-coding:utf-8 -*

print ("hello world")
annee = input("Saisissez une ann�e : ") 
annee = int(annee) # Risque d'erreur si l'utilisateur n'a pas saisi un nombre

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
   print("L'ann�e saisie est bissextile.")
else:
   print("L'ann�e saisie n'est pas bissextile.")
