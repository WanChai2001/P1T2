#include <stdio.h>
int main (){
	int F, B, N;
	printf("Please enter your number =");
	scanf("%d",&N);
	while(N >99 or N < 1)
	{
		 printf("Please enter your number =");
		 scanf("%d",&N);
    }
	F = N/10;
	B = N%10;
	if (F ==7 or B == 7)
	{
		printf("BUZZ");
    }
	else if (N%7 == 0)
	{
		printf("BUZZ-BUUZZ");
    }
	else
    	printf("number =%d",N);
}

