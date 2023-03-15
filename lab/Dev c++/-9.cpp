#include<stdio.h>
#include<string.h>
#include<conio.h>
int main (){
	float avg = 0;
	float max = 0;
	float min = 100;
	char h[30];
	char l[30];
	int i = 0;
	int n = 0;
	printf("Enter your number :");
	scanf("%d" ,&n);
	char name[30];
	float number[n];
	while (i < n){
		printf("Enter Student Name [%d] : ",i);
		scanf("%s",&name);
		printf("Enter Student number [%d] : ",i);
		scanf("%f",&number[i]);
		if (max < number[i]){
			strcpy(h,name);
			max = number[i];
		}
		if (min > number[i]){
			strcpy(l,name);
			min = number[i];
		}
		avg = avg + number[i];
		i += 1;
}
avg = avg / n;
printf("max score is %s %5.2f \n" ,h,max);
printf("min score is %s %5.2f \n" ,l,min);
printf("average score is %s %5.2f \n" ,avg);
}
	
	
