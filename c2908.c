#include <stdio.h>

int main() {
	int a, b;
	scanf("%d %d", &a, &b);

	int ra, rb;
	ra = a/100 + a%100/10*10 + a%10*100;
	rb = b/100 + b%100/10*10 + b%10*100;

	if(ra>rb)
		printf("%d", ra);	
	else
		printf("%d", rb);

	return 0;
}
