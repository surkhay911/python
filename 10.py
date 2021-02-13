def f(x):
    if (x<-5):
        return (x**2)
    elif (x>=5):
        return (x**3)
    else:
        return (x**4)

x = int(input("введите a= "))
b = int(input("введите b= "))
h = int(input("введите шаг h= "))

while(x<=b):
    print("x= ",x,"f(x)= ",f(x))
    x+=h
