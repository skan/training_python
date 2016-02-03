

def table (base, debut, fin, inc):
   mult = debut
   for mult in range (fin) :
      print ("{} * {} = {} ".format(base, mult, base * mult))
      mult = mult + 1

table (2,1,10,1)
