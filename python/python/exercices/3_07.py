
def unDictionnaire (**dico):
    for key, value in dico.items():
        print (key, value)
    return dico

myDico = {"nom":"hamza", "prenom":"skander", "age":35}
unDictionnaire(**myDico)
print ("{}".format ("5*-"))
print (unDictionnaire(**myDico))

