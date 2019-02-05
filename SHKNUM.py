a,j=[],1 
while(j<1e9):
    a.append(j)
    j*=2
a.append(j)
a.append(j*2)
a.append(j*4)
q=len(a)
b=[a[i]+a[j] for i in range(q) for j in range(q) if i!=j]
b.sort()
q=len(b)
def binpar(p,r,s):
    b,e=0,r  
    while b!=e:
        m=(b+e)//2
        if p[m]<s:
            b=m+1 
        else:
            e=m 
    return b
t=int(input())
while t>0:
    t-=1 
    n=int(input())
    j=binpar(b,q,n)
    if j==0:
        c=b[0]-n
    else:
        c=min(b[j]-n,n-b[j-1])
    print(c)