# -*-coding:Latin-1 -*

import sys
filtre = sys.argv[-1]
print("filtre =", filtre)

file = open("monExemple.txt","r")
content=file.readlines()
print(" all file content = ", content, "\n")
#listContent=content.split("=")
#print(listContent[1])

def maFonction (filtre):
    for element in content :
        test=element.split("=")
        print (test)
        if test[0]==filtre:
            result="=".join(test[1:])
    return result

    
if __name__ != '__main__':
    result=maFonction(filtre)    
    try: 
        print(result)
    except:
        print ("no", filtre, " here")
    
