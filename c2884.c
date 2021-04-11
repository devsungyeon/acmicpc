#include <stdio.h>

int main() {
	int h, m;
	scanf("%d %d", &h, &m);
	if(m < 45) {
		h += 23;
		h %= 24;
	}
	m += 15;
	m %= 60;
	
	printf("%d %d", h, m);
	return 0;
}
