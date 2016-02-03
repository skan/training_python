class Personne:
    
    """Classe d�finissant une personne.
    
    Elle poss�de comme attributs :
    nom -- le nom de la personne
    prenom -- son pr�nom
    age -- son �ge
    lieu_residence -- son lieu de r�sidence
    
    Le nom et le pr�nom doivent �tre pass�s au constructeur."""
    
    def __new__(cls, nom, prenom):
        print("Appel de la m�thode __new__ de la classe {}".format(cls))
        # On laisse le travail � object
        return object.__new__(cls, nom, prenom)
    
    def __init__(self, nom, prenom):
        """Constructeur de notre personne."""
        print("Appel de la m�thode __init__")
        self.nom = nom
        self.prenom = prenom
        self.age = 23
        self.lieu_residence = "Lyon"
