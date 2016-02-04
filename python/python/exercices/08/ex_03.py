
def creer_plus(ajout):
    def plus (increment):
        return increment + ajout
    return plus
    
p  = creer_plus(23)
q  = creer_plus(43)

print (p(100), q(100))
