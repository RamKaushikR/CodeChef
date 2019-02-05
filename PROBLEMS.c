#include<stdlib.h>
#include<stdio.h>
void merge(int a[], int b[], int l, int m, int r)
{
    int i,j,k;
    int n1=m-l+1;
    int n2=r-m;
    int l1[n1],l2[n1],r1[n2],r2[n2];
    for (i = 0;i<n1;i++){
        l1[i]=a[l+i];
        l2[i]=b[l+i];
    }
    for (j=0;j<n2;j++){
        r1[j]=a[m+1+j];
        r2[j]=b[m+1+j];
    }
    i = 0;
    j = 0;
    k = l;
    while(i<n1 && j<n2)
    {
        if(l1[i]<=r1[j])
        {
            a[k]=l1[i];
            b[k]=l2[i];
            i++;
        }
        else
        {
            a[k]=r1[j];
            b[k]=r2[j];
            j++;
        }
        k++;
    }
    while(i<n1)
    {
        a[k]=l1[i];
        b[k]=l2[i];
        i++;
        k++;
    }
    while(j<n2)
    {
        a[k]=r1[j];
        b[k]=r2[j];
        j++;
        k++;
    }
}
void mergeSort(int a[], int b[], int l, int r)
{
   if(l<r)
   {
      int m=(l+r-1)/2; 
      mergeSort(a,b,l,m);
      mergeSort(a,b,m+1,r);
      merge(a,b,l,m,r);
   }
}
void print(int a[], int n)
{
    for(int i=0;i<n;i++)
        printf("%d\n", a[i]);
}
int main()
{
    long int p,q;
    int s;
    scanf("%ld%d",&p,&s);
    q=p;
    int sc[s],ns[s],a[p],b[p];
    while(q){
        int n=0;
        for(int i=0;i<s;i++)
            scanf("%d",&sc[i]);
        for(int i=0;i<s;i++)
            scanf("%d",&ns[i]);
        mergeSort(sc,ns,0,s-1);
        for(int i=0;i<s-1;i++){
            if(ns[i]>ns[i+1])
                n++;
        }
        a[p-q]=n;
        b[p-q]=p-q+1;
        q--;
    }
    mergeSort(a,b,0,p-1);
    print(b,p);
    return 0;
}