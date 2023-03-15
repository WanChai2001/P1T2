#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
typedef struct stdstruct stdtype;
struct employeesstruct{
     char pas[30];
	 char fname[30];
	 char lname[30];
	 int age;
	 int month;
	 char sec[30];
}employees;

int main(){
	FILE*fp,*fp2;
	char file1[30],file2[30];
	printf("File name for read : ");
	gets(file1);
	printf("File name for write :");
	gets(file2);
	
	fp = fopen(file1 , "r+");
	if(file1 == NULL){
		printf("error");
		exit(1);
	}
	fp2 = fopen(file2 , "w");
	while(fread(&employees, sizeof(employees),1,fp) == 1){
		employees.month = employees.month + (employees.month * 0.05);
		fwrite(&employees , sizeof(employees),1,fp2);
	}
	fclose(fp);
	fclose(fp2);
	
	fp = fopen(file1 , "r");
	if(file1 == NULL){
		printf("error");
		exit(1);
	}
	int i = 0;
	while(fread(&employees , sizeof(employees), 1 , fp) == 1){
		printf("information of employee from [%s] No.[%d]\n",file1,i+1);
		printf("Employee ID = %s \n",employees.pas);
		printf("Employee FirstName = %s \n",employees.fname);
		printf("Employee Sername = %s \n",employees.lname);
		printf("Employee Age = %d \n",employees.age);
		printf("Employee Salary = %d \n",employees.month);	
		printf("Employee Department = %s \n",employees.sec);
		printf("\n");
		i++;
	}
	fclose(fp);
	
	fp2 = fopen(file2 , "r");
	if(file2 == NULL){
		printf("error");
		exit(1);
	}
	int j = 0;
	while(fread(&employees , sizeof(employees), 1 , fp2) == 1){
		printf("information of employee from [%s] No.[%d]\n",file1,j+1);
		printf("Employee ID = %s \n",employees.pas);
		printf("Employee FirstName = %s \n",employees.fname);
		printf("Employee Sername = %s \n",employees.lname);
		printf("Employee Age = %d \n",employees.age);
		printf("Employee Salary = %d \n",employees.month);	
		printf("Employee Department = %s \n",employees.sec);
		printf("\n");
		j++;
	}
	fclose(fp2);
	
	
	
}
