#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <string.h>
typedef struct nodestruct *number;
struct nodestruct {
	char str;
	number next;                                        
};

int main(){
	int i;
	number temp,n1,n2,n3,first;
	first = NULL;
	i = 1;
	while (i<=4){
		temp = (number)malloc(sizeof(nodestruct));
		printf("Number of coefficients (%d) = ",i);
		scanf("%d",&n1);
		printf("Number of Exponent (%d) = ",i);
		scanf("%d",&n2);
		temp -> next = n1;
		n1 -> next = n2;
		n2 -> next = n3;
		n3 -> next = NULL;
		first = temp;
		i = i + 1;
	}
	i = 0;
	while(i<4){
		printf("%.1f|%d\n",first -> str);
		first = first -> next;
		i++;
	}
	first = temp;	
}

