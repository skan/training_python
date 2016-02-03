from verif_m import verif

def somDiv(n):
    tot = 0
    for i in range (1,n):
        if n % i == 0:
            tot = tot + i 
    return tot
            
def estPremier(n):
    return True if somDiv(n) == 1 else False
        
def estParfait(n):
    return True if somDiv(n) == n else False

def estChanceux(a):
    for n in range (a-1):
        if estParfait(a + n + n*n) :
            return True
    return False
    
    """
nombre = 13
div = somDiv (nombre)

print ("div de {} : {} --> premier : {} --> parfait : {}".format(nombre,somDiv(nombre), estPremier(nombre), estParfait(nombre)))

for i in range (1,100):
    if (estParfait(i)):
        print ("div de {} : {} --> premier : {} --> parfait : {}".format(i,somDiv(i), estPremier(i), estParfait(i)))
        
for i in range (1,100):
    if (estChanceux(i)):
        print ("div de {} : {} --> premier : {} --> chanceux : {}".format(i,somDiv(i), estPremier(i), estChanceux(i)))

"""
# Auto-test ---------------------------------------------------------
if __name__=='__main__':
    verif(somDiv(12), 16, comment="Somme des diviseurs propres de 12 : ")
    verif(estParfait(6), True, comment="6 est-il parfait : ")
    verif(estPremier(31), True, comment="31 est-il premier : ")
    verif(estChanceux(11), True, comment="11 est-il chanceux : ")
