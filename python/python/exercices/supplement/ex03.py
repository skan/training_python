
myList=[]
tot = 0
while 1:
    nombre = int(input ("specifier un numero: "))
    if (nombre == 0 or nombre < 0):
        print ("breaking")
        break
    else:
        myList.append(nombre)

for element in myList:
    tot += element

print (tot)
