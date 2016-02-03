
class MaClasse:
    def __init__(self):
        self.x = 23
        self.y = self.x + 5
    def affiche (self):
        self.z = 42
        print ("y = {} & z = {}".format(self.y,self.z))

class Vecteur2D:
    def __init__ (self, x=0, y=0):
        self.x = x
        self.y = y
    def __repr__(self): # appelle qd on appelle l'objet 
        return "through rep vector ({},{})".format(self.x,self.y)
    def __str__ (self): # ecrase repr qd elle est defnie, appele qd print (obj)
        return "through str :vector ({},{})".format(self.x,self.y)
    def affiche (self): 
        print ("through affiche() :vector ({},{})".format(self.x,self.y))
    def __getattr__(self, nom): # Appele si l'attribut n'existe pas
        print ("getattr msg: {} n'existe pas".format(nom))
    def __add__ (self, obj):
        newVect = Vecteur2D()
        newVect.x = self.x + obj.x
        newVect.y = self.y + obj.y
        return newVect


monObjet = MaClasse()
monObjet.affiche()

monVect = Vecteur2D(1,2)
monVect2 = Vecteur2D(5,6)
totVect = Vecteur2D()

print (monVect2.__dict__ )
monVect2.__dict__ 
print(monVect2)
monVect2
monVect2.affiche()
monVect2.attributQuiNexistePas
monVect2.x
print (monVect2 + monVect)
