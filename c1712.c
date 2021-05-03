#include <stdio.h>

int main() {
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	int i = 0 ;
	if(b>=c) {
		printf("-1");
		return 0;
	}
	
	printf("%d", (a/(c-b)+1));
	return 0;
}
