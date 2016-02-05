
class ArrangedDico:
    def __init__(self, **articles):
        self.dicoKey = []
        self.dicoValues = []
        if (articles is not None):
            for key, value in articles.items():
                print (key,value)
                self.dicoKey.append(key)
                self.dicoValues.append(value) 
legumes= {"oranges":22,"fraise":10}
monDico = ArrangedDico(oranges=25, pommes=32)
monDico = ArrangedDico(**legumes)

