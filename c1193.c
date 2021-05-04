#include <stdio.h>

int f(int i) {
	return 1+(i-1)*i/2;
}

int main() {
	int x;
	scanf("%d", &x);

	int r = 0;
	while(f(++r) <= x);
	r--;
	if(r%2 == 0)
		printf("%d/%d", 1+x-f(r), r-x+f(r));
	else
		printf("%d/%d", r-x+f(r), 1+x-f(r));	
	return 0;
}
