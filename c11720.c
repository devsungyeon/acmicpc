#include <stdio.h>

#define MAX 100

int main() {
	int n;
	scanf("%d", &n);
	char arr[MAX];

	scanf("%s", arr);

	int sum = 0 ;
	for(int i = 0 ; i < n ; i++ ) {
		sum += (arr[i]-'0');
	}
	printf("%d", sum);

	return 0;
}
