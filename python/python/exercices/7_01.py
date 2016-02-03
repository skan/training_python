# -*- coding: UTF-8 -*-
"""Les dictionnaires en Python (2/2)."""
# fichier : cours4_42.py
# auteur : Bob Cordeau
dico = {"Au":{"Te/Tf":(2970, 1063),
"N/M atomique":(79, 196.967)
},
"Ga":{"Te/Tf":(2237, 29.8),
"N/M atomique":(31, 69.72)
}
}
# programme principal -----------------------------------------------
print(dico["Au"], "\n")
print(dico["Ga"]["Te/Tf"], "\n")
print("Numero atomique de l'or :", dico["Au"]["N/M atomique"][0], "\n")
print("Masse atomique de l'or :", dico["Au"]["N/M atomique"][1])