
def compterMot(chaine):
    tot = 0
    localList = chaine.split()
    for e in localList:
        tot = tot + 1
    return tot

maChaine="bonjour, je compte le nombre de mots pour cet exercices"
a = compterMot (maChaine)
print (maChaine, a)


