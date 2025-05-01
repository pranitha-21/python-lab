#include <stdio.h>
void main(){
	float principle,time,rate,simpleinterest;
	
	printf("Enter Principle:");
	scanf("%f",&principle);
	
	printf("Enter Time:");
	scanf("%f",&time);
	
	printf("Enter Rate:");
	scanf("%f",&rate);
	
	simpleinterest=(principle*time*rate)/100;
	printf("simple interest is %f",simpleinterest);
	
	}
