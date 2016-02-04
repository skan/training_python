TVA = 1.18
while (1):
    ht = float(input ("donner le prix ht: "))
    if (ht == 0):
        break
    print ("\t ---> ttc = {}".format (ht*TVA))

