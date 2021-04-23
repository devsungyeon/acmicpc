#include <stdio.h>

int arr[10001];

void selfnum(int a) {
	if(a > 10000)
		return;
	int sum = a;
	while(a) {
		sum += a%10;
		a = a/10;
	}
	arr[sum] = 0;
	selfnum(sum);
}

int main() {
	for(int i = 1; i<= 10000; i++ ) 
		arr[i] = 1;
	for(int i = 1; i<= 10000; i++ ) 
		if(arr[i] == 1) 
			selfnum(i);

	for(int i = 1; i<= 10000; i++ )
		if(arr[i] == 1)
			printf("%d\n", i);
	
	return 0;
}
