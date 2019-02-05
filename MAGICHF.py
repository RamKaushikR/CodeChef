# cook your dish here
t=int(input())
while t>0:
    t-=1 
    n,x,s=map(int,input().split())
    while s>0:
        s-=1 
        a,b=map(int,input().split())
        if x==a:
            x=b 
        elif x==b:
            x=a 
    print(x)