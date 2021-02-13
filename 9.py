def f(x):
    return (1/x)

x = int(input("введите а="))
b = int(input("введите b="))
h = int(input("введите шаг h="))

while (x<=b):
    try:
        print("x= ",x,"f(x)= ",f(x))
        x+=h
    except ZeroDivisionError:
        print("x= ",x,"f(x)= Nan")
        x+=h
