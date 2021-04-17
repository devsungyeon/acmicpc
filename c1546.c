#include <stdio.h>

#define MAX_LENGTH 1000

int main() {
	int n;
	scanf("%d", &n);
	
	double arr[n];
	double max = 0;
	for(int i = 0 ; i < n ; i++ ) {
		scanf("%lf", &arr[i]);
		if(arr[i] > max)
			max = arr[i];
	}
	for(int i = 0 ; i < n ; i++ ) {
		arr[i] = arr[i] / max * 100;
	}
	double sum=0;
	for(int i = 0 ; i < n ; i++ ) {
		sum += arr[i];
	}

	printf("%0.2lf", sum/n);

	return 0;
}
