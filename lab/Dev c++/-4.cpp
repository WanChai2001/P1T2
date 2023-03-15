#include <stdio.h>
int main (){
	int n,a,sum	;
	int i=0;
	printf("input n = ");
	scanf("%d",&n);
    printf ("input a = ");
    scanf("%d",&a);
    sum = n;
	while (sum >= a ){
	    sum = sum - a;
		i=i+1;
	}
	printf("i = %d\n",i);
	printf("sum = %d",sum);
	 
}
