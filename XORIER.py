# cook your dish here
t=int(input())
while t>0:
    t-=1 
    n=int(input())
    a=[int(x) for x in input().split()]
    e,o=[],[]
    de,do=dict(),dict()
    for i in a:
        if i%2==0:
            e.append(i)
            if i in de:
                de[i]+=1 
            else:
                de[i]=1 
        else:
            o.append(i)
            if i in do:
                do[i]+=1 
            else:
                do[i]=1
    le,lo=len(e),len(o)
    se,so=le*(le-1)//2,lo*(lo-1)//2
    for i in e[:le-1]:
        se=se-de[i]+1
        if i%4==0:
            if i+2 in de:
                se=se-de[i+2]
        else:
            if i-2 in de:
                se=se-de[i-2] 
        de[i]-=1 
    for i in o[:lo-1]:
        so=so-do[i]+1
        if i%4==1:
            if i+2 in do:
                so=so-do[i+2] 
        else:
            if i-2 in do:
                so=so-do[i-2] 
        do[i]-=1
    print(se+so)