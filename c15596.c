#include <stdio.h>

long long sum(int *a, int n) {
	long long ret=0 ; 
	
	for(int i = 0 ; i < n ; i++ ) {
		ret += *a;
		a=a+1;
	}

	return ret;
}

int main() {
	int arr[10] = {1,2,3,4,5,6,7,8,9,10};
	int n = 10;

	int answer = 0;

	answer = sum(arr, n);

	printf("%d\n", answer);

	return 0;
}
