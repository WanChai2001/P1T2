#include<stdio.h>
int main (){
	int n;
	int a;
	int one;
	int two;
	printf("n = ");
	scanf("%d",&n);
	printf("a = ");
	scanf("%d",&a);
	one = n;
	two = a;
	while (n != a){
		if (n > a){
			n = n - a;
		}
		else
			a = a - n;
	}
	printf("Greatest Commond Division of %d and %d is %d",one,two,n);
}
