# cook your dish here
mod=int(1e9+7)
t=int(input())
while t>0:
    t-=1 
    n,w=map(int,input().split())
    if w>8 or w<-9:
        s=0
    else:
        if w<0:
            w=-(w+1) 
        s=(((9-w)%mod)*pow(10,n-2,mod))%mod
    print(s)