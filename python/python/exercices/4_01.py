# -*-coding:UTF-8 -*

def exercice_01():
    liste =[17, 38, 10, 25, 72]
    print liste
    liste.sort()
    print liste
    liste.append(12)
    print liste
    liste.reverse()
    print liste
    liste.remove(38)
    print liste
    print liste[2:4]
    print liste[:3]
    print liste[3:]
    print liste[:]
    print liste.index(17)
    print liste[-1]

def exercice_02 ():
    truc = []
    machin = [0.0]*5
    print truc
    print machin
    print("range(4) =", range(4))
    print("range(4, 8) =", range(4, 8))
    print("range(2, 9, 2) =", range(2, 9, 2), "\n")
    chose = range(6)
    print chose
    print (3 in chose)
    print (6 in chose)

def exercice_03():    
    chose = range(6)
    print chose
    chose = [ element+3 for element in chose ]
    print chose

def exercice_04():    
    chose = range(6)
    print chose
    chose = [ element+3 for element in chose if element >= 2 ]
    print chose

def exercice_04_correction():
    result3 = []
    for i in range(6):
        if i >= 2:
            result3.append(i+3)
    print(" boucle for ".center(50, '-'))
    print(result3, '\n')
    result4 = [i+3 for i in range(6) if i >= 2]
    print(" forme 2 ".center(50, '-'))
    print(result4)

def exercice_05():    
    liste1 = ["a","b","c"]
    liste2 = ["d","e"]
    liste3=zip(liste1,liste2)
    liste3 = liste1 + liste2
    liste3 =[i+j for i in liste1 for j in liste2]
    print(liste3)

def exercice_06():
    a = range(10)
    i = 0
    print(reduce(lambda x,y : x+y, a))
    b = [i+j for i in a ]
    
def exercice_07():
    X={'a','b','c','d'}
    Y={'s',"b",'d'}
    print X 
    print Y
    print('c' in X)
    print (X-Y)
    print(Y-X)
    print("X | Y: ", X | Y)
    print("Y|X  : ", Y | X)
    print("X & Y: ", X & Y)
    
def compterMots(mot):
    dict={}
    listeMots=mot.split()        
    for mot in listeMots:
        if mot in dict:
            dict[mot] = dict[mot] + 1
        else:
            dict[mot]= 1
    return dict
    
def exercice_09():
    dico={}
    dico ={"Au":"val1","Ga":"val2"}

print (compterMots("bla bla bla test skander skander oops"))
