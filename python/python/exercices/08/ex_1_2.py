
class Rectangle:
    def __init__(self, longueur = 4, largeur = 2):
        self.longueur = longueur
        self.largeur = largeur
        self.nom = "rectangle"
    def surface (self):
        print ("surface = {}".format(self.longueur * self.largeur))
    def affiche (self):
        print ("{}_{}x{} et surface = {}".format(self.nom,self.longueur, self.largeur,self.longueur * self.largeur))

class Carre (Rectangle):
    def __init__(self):
        Rectangle.__init__(self, 4,4)
        self.nom = "carre"

class Point :
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({},{})".format(self.x,self.y)

class Segment:
    def __init__(self,x1=2,y1=3,x2=4,y2=5):
        self.orig = Point(x1,y1)
        self.extrem = Point(x2,y2)
    def __str__(self):
        return ("{} --> {}".format(self.orig,self.extrem))

myRect = Rectangle(3,9)
myRect.affiche()
myCar = Carre()
myCar.affiche()

mySeg = Segment(1,2,3,4)
print (mySeg)
