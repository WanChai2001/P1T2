#include<stdio.h>
int main(){
	int r;
	int c;
	int i;
	int j;
	int MatrixA[100][100],MatrixB[100][100],Sum[100][100],Negate[100][100];
	do
	{
		printf("Enter Your row = ");
		scanf("%d",&r);
		printf("Enter Your colum = ");
		scanf("%d",&c);
	}while (r<1 or c<1);
	printf("Enter element of Metrix[A]\n");
	for (i=0;i<r;i=i+1)
	{
		for (j=0;j<c;j=j+1)
		{
			printf("Enter each element of Matrix[A] : ");
			scanf("%d",&MatrixA[i][j]);
		}
	}
	printf("\nEnter element of Metrix[B]\n");
	for (i=0;i<r;i=i+1)
	{
		for (j=0;j<c;j=j+1)
		{
			printf("Enter each element of Matrix[B] : ");
			scanf("%d",&MatrixB[i][j]);
		}
	}
	printf("\n");
	printf("\nYour element of Matrix[A] is \n[");
	for (i=0;i<r;i=i+1)
	{
		printf("(");
		for (j=0;j<c;j++)
		{
			printf("%d",MatrixA[i][j]);
			if (j<c-1)
			{
				printf(",");
			}
		}
		printf(")");
		if (i<r-1)
		{
			printf("\n");
		}
	}
	printf("]");
	printf("\n");
	printf("\nYour element of Matrix[B] is \n[");
	for (i=0;i<r;i=i+1)
	{
		printf("(");
		for (j=0;j<c;j++)
		{
			printf("%d",MatrixB[i][j]);
			if (j<c-1)
			{
				printf(",");
			}
		}
		printf(")");
		if (i<r-1)
		{
			printf("\n");
		}
	}
	printf("]");
	printf("\n\nYour sum of two Matrix is \n[");
	for (i=0;i<r;i=i+1)
	{
		printf("(");
		for (j=0;j<c;j++)
		{
			Sum[i][j]=MatrixA[i][j]+MatrixB[i][j];
			printf("%d",Sum[i][j]);
			if (j<c-1)
			{
				printf(",");
			}
		}
		printf(")");
		if (i<r-1)
		{
			printf("\n");
		}
	}
	printf("]");
	printf("\n");
	printf("\n\nYour minus of two Matrix is \n[");
	for (i=0;i<r;i=i+1)
	{
		printf("(");
		for (j=0;j<c;j++)
		{
			Sum[i][j]=MatrixA[i][j]-MatrixB[i][j];
			printf("%d",Sum[i][j]);
			if (j<c-1)
			{
				printf(",");
			}
		}
		printf(")");
		if (i<r-1)
		{
			printf("\n");
		}
	}
	printf("]");
	printf("\n");
	
}
