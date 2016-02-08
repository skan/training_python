
class ArrangedDico:
    def __init__(self, **articles):
        self.dicoKey = []
        self.dicoValues = []
        if (articles is not None):
            for key, value in articles.items():
                self.dicoKey.append(key)
                self.dicoValues.append(value) 
    def __str__(self):
        ret_str = "{"
        lengh = len (self.dicoValues)
        for i in range (lengh):
            ret_str+= "'{}':{},".format(self.dicoKey[i],self.dicoValues[i]) 
        ret_str = ret_str[:-1]
        ret_str+= "}"
        return ret_str
    def __delitem__(self,value):
       idx = self.dicoKey.index(value)
       print (idx)
        
legumes= {"oranges":22,"fraise":10}
monDico = ArrangedDico(oranges=25, pommes=32)
monDico = ArrangedDico(**legumes)

print (monDico)
del monDico["oranges"]
print (monDico)

