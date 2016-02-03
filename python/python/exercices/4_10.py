
def pile(*data):
    p = []
    if not data:
        return p
    for element in data:
        p.append(element)
    return list(p)

def depile(data):
    data.pop()
    
def empile(data,a):
    data.append(a)

l = list(range(10))

#pile (*l)
#empile(*l)
l=pile(1,2,3)
print (l)
empile(l,4)
print (l)
depile (l)
print (l)
