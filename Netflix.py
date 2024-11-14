tc=int(input())
for i in range(tc):
    x,y,z,k=input().split()
    a=int(x)
    b=int(y)
    c=int(z)
    X=int(k)
    arr=[a,b,c]
    flag=0
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[i]+arr[j]>=X):
                flag=1
            
    if flag==1:
        print("YES")
    else: print("NO")
