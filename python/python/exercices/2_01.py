# -*-coding:UTF-8 -*

# ex 3 ? 
def tabe(base, debut, fin, inc):
   mult = debut
   while  mult < fin:
        print("{} x {} {}".format(base,mult,base*mult))
        mult += inc
  

def cube(x):
    return x*x*x

def exercice_3():
    tabe(7,2,13,2)  
    a = 9
    print ("cube de {} = {}".format(a,cube(a)))

def somme (*nombre):
    somme=0
    for element in nombre:
        somme += element
    return somme

def somme_3 (a,b,c):
    return a+b+c

def exercice_05 ():
    print ("total est {}".format(somme(5,5,4,1)))
    print ("total est {}".format(somme(5,5,4,1,3,1,1)))

    add_list = [6,3,2]
    print ("total est {}".format(somme_3(*add_list)))

def monDictionnaire(**dico):
    for key,value in dico.items():
        print ("sk {} {} ".format(key,  value))
    return dico
        
myDic = {"1":"value1", "2":"value2"}
print(monDictionnaire(**myDic))
