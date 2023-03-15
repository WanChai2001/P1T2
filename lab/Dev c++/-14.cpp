struct carstruct {
	char ID[30],name[30],age[30],salary[30];
	int balance;
}position[30];
#include<stdio.h>
#include<conio.h>
int main(){
	int n,b,i,s;
	printf("Number of employees = ");
	scanf("%d",&n);
	while (n <= 0){
		printf("Number of employees = ");
		scanf("%d",&n);
	}
	for(i = 0;i < n;){
		printf("Employees code = ");
		scanf("%d",&position[i].ID);
		printf("Employees name = ");
		scanf("%s",&position[i].name);
		printf("Employees age = ");
		scanf("%s",&position[i].age);
		printf("Employees salary = ");
		scanf("%s",&position[i].salary);
	}
	for (i = 0; i < n; i = i + 1){
	printf("Employees code = %d \n",position[i].ID);
	printf("Employees name = %s \n",position[i].name);
	printf("Employees age = %d \n",position[i].age);
	printf("Employees salary = %s \n",position[i].salary);
	}
}

