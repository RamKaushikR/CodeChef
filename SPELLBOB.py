t=int(input())
while t>0:
    t-=1 
    a=input()
    b=input()
    bc,oc,cc=0,0,0
    for i in range(3):
        if a[i]=='b' or b[i]=='b' or a[i]=='o' or b[i]=='o':
            cc+=1 
        if a[i]=='b' or b[i]=='b':
            bc+=1 
        if a[i]=='o' or b[i]=='o':
            oc+=1
    if cc==3 and bc>=2 and oc>=1:
        print("yes")
    else:
        print("no")