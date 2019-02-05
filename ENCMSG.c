#include <stdio.h>

int main(void) {
	// your code goes here
	int t,n;
	char s[100];
	scanf("%d",&t);
	while(t--){
	    scanf("%d",&n);
	    scanf("%s",s);
	    for(int i=0;i<n-1;i+=2){
	        char t=s[i];
	        s[i]=s[i+1];
	        s[i+1]=t;
	    }
	    for(int i=0;i<n;i++){
	        s[i]=219-s[i];
	    }
	    printf("%s\n",s);
	}
	return 0;
}