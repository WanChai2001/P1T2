#include <stdio.h>
int main (){
	int n, sum = 0 , i = 1;
	printf ("enter your number = ");
	scanf("%d",&n);
	while (i <= n ){
		sum = sum + i;
		printf ("%d\n",i);
		i++;
		}
	printf("sum = %d" ,sum);
}
	
