#include <stdio.h>

int main() {
	int max = 0;
	int tmp, idx;
	scanf("%d", &tmp);
	idx = 1;
	for(int i = 2 ; i <= 9 ;i++ ) {
		scanf("%d", &tmp);
		if(tmp > max) {
			max = tmp;
			idx = i;
		}
	}
	printf("%d\n%d", max, idx);
	return 0;
}
