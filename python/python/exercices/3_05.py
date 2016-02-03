
def somme (*element):
    tot = 0
    e = 10
    print ("test", e)
    for e in element :
        tot = tot + e
    return tot

sk_test = {1,8,3}
sk_tuple = (1,8.5,3,10)
print ("somme = {}".format (somme(2,8,5)))
print ("somme = {}".format (somme(*sk_test)))
print ("somme = {}".format (somme(*sk_tuple)))

