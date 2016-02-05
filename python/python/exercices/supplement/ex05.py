
nbOfDiv  = 0
nb = int(input ("donnez un nombre: "))
rest = 1
while (rest != 0):
    rest = nb % 2
    nb = nb // 2
    nbOfDiv  += 1
    

print (nbOfDiv)
