#include<stdio.h>
int main (){
	int n;
	int i = 0;
	float min,max,avg,sum = 0,Rainfall [12];
	printf("Enter the number of months = ");
	scanf("%d",&n);
	while (i < n){
		printf("Rainfall[%d] = ",i);
		scanf("%f",&Rainfall[i]);
    	while (Rainfall[i] < 0){
        	printf("Invalid Rainfall \n ");
        	printf("Rainfall[%d] = ",i);
			scanf("%f",&Rainfall[i]);
		}	
		sum = sum + Rainfall[i];
    	i = i + 1;
	}
	avg = sum / 12;
	max = Rainfall[0];
	min = Rainfall[0];
	for(i = 1; i<12; i = i + 1){
    	if (max < Rainfall[i])
        		max = Rainfall[i];
    	if (min > Rainfall[i])
        		min = Rainfall[i];
	}
	printf("max = %f\n",max);
	printf("min = %f\n",min);
	printf("average = %f\n",avg);
}
	
	
