
pi = 3.14
def cube (x):
    return x*x*x

def volumeSphere (r):
    return pi*cube(r)

x = 5
r = 4

print ("cube of {} is {}".format (x,cube (x)))
print ("volume  of r={} is {}".format (r,volumeSphere (r)))
