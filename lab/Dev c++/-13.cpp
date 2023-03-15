struct carstruct {
	char code[30],name[30],account[30],limit[30],category [30],surname [30];
	int balance;
}bank[30];
#include<stdio.h>
#include<conio.h>
int main(){
	int n,b,i,s;
	printf("numbar = ");
	scanf("%d",&n);
	while (n <= 0){
		printf("number = ");
		scanf("%d",&n);
	}
	for(i = 0;i < n; i = i + 1){
		printf("Customer code = ");
		scanf("%s",&bank[i].code);
		printf("Customer name = ");
		scanf("%s",&bank[i].name);
		printf("Customer surname = ");
		scanf("%s",&bank[i].surname);
		printf("Deposit account number = ");
		scanf("%s",&bank[i].account);
		printf("Account type / 1. Means savings account and 2. refers to current account. [1/2] = ");
		scanf("%s",&bank[i].category);
		printf("[1/2]");
		scanf("%d",&s);
		if (s == 1){
			printf("Balance = ");
			scanf("%d",&bank[i].balance);
		}
		if (s == 2){
			printf("Balance = ");
			scanf("%d",&bank[i].balance);
			printf("Credit limit = ");
			scanf("%s",&bank[i].limit);
		}
		
	}
	for (i = 0; i < n; i = i + 1){
		printf("Customer code = %s \n",bank[i].code);
		printf("Customer name = %s \n",bank[i].name);
		printf("Customer surname = %s \n",bank[i].surname);
		printf("Account type = %s \n",bank[i].category);
		printf("Deposit account number = %s \n",bank[i].account);
		printf("Credit limit = %s \n",bank[i].balance);
		printf("Balance = %d \n",bank[i].limit);
		
	}
}

