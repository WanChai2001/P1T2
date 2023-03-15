struct carstruct {
	char Brand[30],Gen[30],Color[30];
	int Price;
}car[30];
#include<stdio.h>
int main(){
	int n,i;
	printf("numbar car = ");
	scanf("%d",&n);
	while (n <= 0){
		printf("number car = ");
		scanf("%d",&n);
	}
	for(i = 0; i < n; i = i + 1){
		printf("carBrand = ");
		scanf("%s",&car[i].Brand);
		printf("carGen = ");
		scanf("%s",&car[i].Gen);
		printf("carColor = ");
		scanf("%s",&car[i].Color);
		printf("carPrice = ");
		scanf("%d",&car[i].Price);
	}
	for (i = 0; i < n; i = i + 1){
		printf("carBrand = %s \n",car[i].Brand);
		printf("carGen = %s \n",car[i].Gen);
		printf("carColor = %s \n",car[i].Color);
		printf("carPrice = %d \n",car[i].Price);
		
	}
}

