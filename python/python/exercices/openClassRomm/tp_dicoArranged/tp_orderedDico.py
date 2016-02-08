import copy
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

if __name__ == '__main__':
    legumes= {"oranges":22,"fraise":10}
    monDico = ArrangedDico(oranges=25, pommes=32)
    monDico = ArrangedDico(**legumes)

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
