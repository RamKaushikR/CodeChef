import math
mod=int(1e9+7)
def power(a,b,m):
    r = 1
    while b:
        if b & 1:
            r = (r*a)%m
        b >>= 1
        a = (a*a)%m
    return r
t=int(input())
while t>0:
    t-=1
    a,b,n=map(int,input().split())
    r=(a-b)
    if r<0:
        r=-r
    if r==1:
        g=1 
    elif r==0:
        s=power(a,n,mod)+power(b,n,mod)
        g=s 
    else:
        s=power(a,n,r)+power(b,n,r)
        g=math.gcd(s,r)%mod
    print(g) 