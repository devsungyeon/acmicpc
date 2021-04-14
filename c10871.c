#include <stdio.h>

int main() {
	int n, x;
	scanf("%d %d", &n, &x);
	int input;
	for(int i=0 ;i<n; i++ ) {
		scanf("%d", &input);
		if(x > input)
			printf("%d ",input);
	}
	
	return 0;
}
