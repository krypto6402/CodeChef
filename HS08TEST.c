#include <stdio.h>

int main(void) {
	int a;
	float b;
	
	scanf("%d %f",&a,&b);
	if(((a+0.5)>b)||(a%5!=0))
	printf("%0.2f",b);
	else 
	printf("%.2f",(b-0.50-(float)a));
	
	return 0;
}
