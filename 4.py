import math

def volume(r):
    return (4.0/3*math.pi*r**3)

r1 =  int(input("r1="))
r2 =  int(input("r2="))
r3 =  int(input("r3="))

z = (volume(r1)+volume(r2)+volume(r3))/3
print(z)
