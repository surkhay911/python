b1 = 1
b2 = 2

n = int(input("n="))

for i in range(0,n,1):
    try:
        bn=(b1-b2)/(i-1)**2
        b1=b2
        b2=bn
        print(bn)
    except ZeroDivisionError:
        print("ZeroDivisionError")
