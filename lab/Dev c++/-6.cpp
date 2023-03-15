#include <stdio.h>
int main (){
	int n;
	int i = 1;
	int medal = 0;
	int sum = 0;
	int price;
	int money;
	printf("input n = ");
	scanf("%d",&n);
	while (i <= n){
		printf ("price = ");
		scanf("%d",&price);
		sum = sum + price;
		i = i + 1;
	}
	printf("sum = %d\n",sum);
	printf("money = ");
	scanf("%d",&money);
	while (money < sum){
		printf("Your money lass than price of product ");
		printf("money = ");
		scanf("%d",&money);
	}
	if (money >= sum);
		medal = money - sum;
	printf("medel = %d",medal);
}
