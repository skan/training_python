
def isPair(n):
    if (n % 2 == 0):
        return "pair"
    else:
        return "impair"

nombre = int (input ("donnez un nombre : "))
#print( isPair(nombre))
print ("le nombre {} est {}".format(nombre,isPair(nombre)))
