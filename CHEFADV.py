# cook your dish here
t=int(input())
while t>0:
    t-=1 
    n,m,x,y=map(int,input().split())
    f=0
    if n==1 and m==1:
        f=1 
    elif n==2 and m==2:
        f=1 
    elif n==1:
        if (m-1)%y==0:
            f=1 
    elif m==1:
        if (n-1)%x==0:
            f=1 
    elif x==1 and y==1:
        f=1 
    elif x==1:
        if (m-1)%y==0 or (m-1)%y==1:
            f=1
    elif y==1:
        if (n-1)%x==0 or (n-1)%x==1:
            f=1
    elif n==2:
        if (m-1)%y==1:
            f=1 
    elif m==2:
        if (n-1)%x==1:
            f=1 
    elif n<=x or m<=y:
        f=0
    elif (m-1)%y==0 and (n-1)%x==0:
        f=1
    elif (m-1)%y==1 and (n-1)%x==1:
        f=1 
    if f==1:
        print("Chefirnemo")
    else:
        print("Pofik")