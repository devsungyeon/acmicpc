#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);
	int min, max;
	min = 1000001;
	max = -1000001;

	int input;
	for(int i = 0 ; i < n ;i ++ ) {
		scanf("%d", &input);
		if(input > max)
			max = input;
		if(input < min)
			min = input;
	}
	printf("%d %d", min, max);
	
	
	return 0;
}
