t=int(input())
while t>0:
    t-=1 
    n,k=map(int,input().split())
    a=[int(x) for x in input().split()]
    if sum(a)<k:
        print(2)
    else:
        s=0
        for i in range(n):
            if i%2==0:
                if s<0:
                    s-=a[i]
                else:
                    s+=a[i]
            else:
                if s<0:
                    s+=a[i]
                else:
                    s-=a[i]
        if abs(s)>=k:
            print(1)
        else:
            print(2)