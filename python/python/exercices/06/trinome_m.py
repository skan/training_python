
from math import sqrt

def trinome (a,b,c):
    delta = b**2 - 4*a*c
    if delta < 0 :
        return 0,
    elif delta == 0 :
        return (1,-b / 2*a)
    else :
        return (2, ((-b - sqrt(delta))/2*a), (-b + sqrt(delta))/2*a)

if __name__=='__main__':
   result = trinome(1,-3,2)
   print (result)


    
