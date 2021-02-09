import math
x = float(input("write point x="))
y = float(input("write point y="))

if (x*x+y*y<100):
    print("yes")
elif (x*x+y*y>100):
    print("no")
else:
    print("on the border")
