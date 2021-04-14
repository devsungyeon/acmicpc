#include <stdio.h>

int main() {
	int n, c, result;
	scanf("%d", &n);
	result = n;
	c=0;
	while(1) {
		c++;
		int t, y;
		t = n / 10;
		y = n % 10;
		n = y*10 + (t+y) % 10;
		if(result == n)
			break;
	}
	printf("%d", c);
	return 0;
}
