tc=int(input())
for i in range(tc):
    x,y,z=input().split()
    a=int(x)
    b=int(y)
    c=int(z)
    if a+b<=c:
        print(2)
    elif a+b>c:
        if a<=c:
            print(1)
        else: print(0)
    else: print(0)
