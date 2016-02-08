import copy
class ArrangedDico:
    def __init__(self, base={}, **articles):
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
    def __delitem__(self,name):
       idx = self.dicoKey.index(name)
       del self.dicoKey[idx]
       del self.dicoValues[idx]
       print ("{} is deleted".format(name))
    def __getitem__(self,name):
       idx = self.dicoKey.index(name)
       return self.dicoValues[idx]
    def __setitem__(self,name,value):
        if (name in self.dicoKey):
           idx = self.dicoKey.index(name)
           self.dicoValues[idx]=value
        else:
           self.dicoValues.append(value)
           self.dicoKey.append(name)
    def __contains__(self,name):
        if (name in self.dicoKey):
            return True
    def __len__(self):
        return len(self.dicoKey)
    def sort(self):
        sortedVal = []
        sortedKey =copy.copy(self.dicoKey)
        sortedKey.sort()
        for element in sortedKey:
            idx = self.dicoKey.index(element)
            sortedVal.append(self.dicoValues[idx])
        self.dicoKey = copy.copy(sortedKey)
        self.dicoValues = copy.copy(sortedVal)
    def reverse(self):
        sortedVal = []
        sortedKey = sorted(self.dicoKey,reverse=True)
        for element in sortedKey:
            idx = self.dicoKey.index(element)
            sortedVal.append(self.dicoValues[idx])
        self.dicoKey = copy.copy(sortedKey)
        self.dicoValues = copy.copy(sortedVal)
    def __iter__(self):
        self.current = 0
        return self
    def __next__(self):
        if (self.current+1 > len(self.dicoValues)):
            raise StopIteration
        else:
            self.current += 1
            return self.dicoKey[self.current-1], self.dicoValues[self.current-1]
    def keys(self):
        return self.dicoKey
    def values(self):
        return self.dicoValues

    def items(self):
        for i, key in enumerate(self.dicoKey):
            valeur = self.dicoValues[i]
            yield (key,valeur)
    def __add__(self,newDico):
        if ( type(newDico) is not type (self)):
            raise TypeError ("Impossible d'ajouter {0} & {1}".format(\
                    type(self),type(newDico)))
        else:
            nouveau=ArrangedDico()
            for key,val in self.items():
                nouveau[key]=val
            for key,val in newDico.items():
                nouveau[key]=val
        return nouveau


if __name__ == '__main__':
    fruits = ArrangedDico()
    fruits["pommes"]=52
    fruits["poires"]=34
    fruits["prune"]=128
    fruits["melon"]=15
    print(fruits)
    fruits.sort()
    print(fruits)
    legumes=ArrangedDico(carotte=26,haricot=48)
    print(legumes)
    print (len (legumes))
    legumes.reverse()
    print(legumes)
    fruits=fruits+legumes
    print(fruits)
    del fruits["haricot"]
    print("haricot" in fruits)
    for cle in legumes:
        print (cle)
    print(legumes.keys())

if __name__ == '__main2__':
    legumes= {"oranges":22,"fraise":10}
    fruits={"patates":3,"tomates":8}
    monDico = ArrangedDico(oranges=25, pommes=32)
    monDico = ArrangedDico(**legumes)
    NewDico = ArrangedDico(**fruits)

    print (monDico)
    del monDico["oranges"]
    print (" *** del testing: ",monDico)

    monDico = ArrangedDico(**legumes)
    print (" *** getitem testing: ", end=" ")
    print (monDico)
    a=monDico["oranges"]
    print (a)
    print (" *** setitem testing: ")
    print (monDico)
    monDico["oranges"]=69
    print (monDico)
    monDico["bananes"]=25
    print (monDico)
    print (" *** __contains__: ")
    a="bananes" in monDico
    print(a)
    print (" *** len: ",len(monDico))
    print (" *** sort: ")
    monDico.sort()
    print (monDico)
    print (" *** reverse: ")
    monDico.reverse()
    print (monDico)
    for i,j in monDico:
        print (i,j)
    for key in monDico.keys():
        print (key)
    for val in monDico.values():
        print (val)
    monDico = monDico + NewDico
    print (monDico)
    for key,val in monDico.items():
        print ("using item {} {}".format(key,val))

