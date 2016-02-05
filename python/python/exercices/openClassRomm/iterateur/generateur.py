def intervalle(mini, maxi):
    mini += 1
    while (mini < maxi):
        value = (yield mini)
        if (value is not None):
            mini = value
        mini += 1

a = intervalle (3 ,30)
print(type(a))
for element in a :
    if (element == 15):
        a.send(19)
    if (element == 17):
        a.close()
    print (element, end = " ")
print  ("")
