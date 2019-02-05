#include <stdio.h>
int pos(int a, int b){
    if(a>b)
        return 1;
    else
        return 2;
}
int neg(int a, int b, int n){
    if(n%2==0){
        if(a>b)
            return 2;
        else
            return 1;
    }
    else{
        return(pos(a,b));
    }
}
int apos(int a, int b, int n){
    if(n%2==0){
        return(pos(a,-b));
    }
    else
        return 1;
}
int bpos(int a, int b, int n){
    if(n%2==0){
        return(pos(-a,b));
    }
    else
        return 2;
}
int zero(int a, int b, int n){
    if(a==0){
        if(n%2==0){
            return 2;
        }
        else{
            if(b>0)
                return 2;
            else
                return 1;
        }
    }
    else if(b==0){
        if(n%2==0){
            return 1;
        }
        else{
            if(a>0)
                return 1;
            else
                return 2;
        }
    }
    
}
int main(){
    long int t,a,b,n;
    scanf("%ld",&t);
    while(t--){
        scanf("%ld%ld%ld",&a,&b,&n);
        if(a==b || (a==-b && n%2==0))
            printf("0");
        else if(a==0 || b==0)
            printf("%d",zero(a,b,n));
        else if(a>0 && b>0)
            printf("%d",pos(a,b));
        else if(a<0 && b<0)
            printf("%d",neg(a,b,n));
        else if(a>0 && b<0)
            printf("%d",apos(a,b,n));
        else
            printf("%d",bpos(a,b,n));
        printf("\n");
    }
}