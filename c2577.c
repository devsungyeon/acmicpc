#include <stdio.h>

int main() {
	int a, b, c, multi;
	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);
	multi = a*b*c;

	int arr[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	
	while(multi != 0) {
		int tmp = multi % 10;
		multi = multi / 10;
		arr[tmp]++;
	}

	for(int i = 0 ; i <= 9 ;i++ ) {
		printf("%d\n", arr[i]);
	}

	return 0;
}
