#include<stdio.h>
int main (){
	int n;
	printf("number =");
	scanf("%d",&n);
	if (n < 0);{
    printf("Please enter your number =");
	scanf("%d",&n);
    }
	if (n % 2 == 0){
    printf("even");
	}
else
    printf("odd");
}
