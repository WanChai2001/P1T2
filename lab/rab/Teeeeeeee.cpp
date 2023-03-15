#include<stdio.h>
int main() {
	int n;
	int i = 0;
printf("number = ");
scanf ("%d",&n);
if (n > 0){
    printf("positive number");
	while (i < n){
        i = i + 1;
        printf("%d\n",i);
    	}
	}
if (n < 0){
    printf("negative number");
    while (i > n){
        i = i - 1;
        printf("%d\n",i);
    	}
	}
if (n == 0){
    printf("it is zero number");
	}	
else
    printf("number",n);
}
