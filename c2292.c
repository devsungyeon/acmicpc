#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);

	if(n <= 2) {
		printf("%d", n);
		return 0;
	}
	int i = 3;
	while( (2+3*(i-2)*(i-1)) <= n )
		i++;
	printf("%d", --i);

	return 0;
}
