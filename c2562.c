#include <stdio.h>


int main() {
	int max = 0;
	int tmp, idx;
	idx = 0;
	for(int i = 1 ; i <= 9 ;i++ ) {
		scanf("%d", &tmp);
		if(tmp > max) {
			max = tmp;
			idx = i;
		}
	}
	printf("%d\n", max);
	printf("%d", idx);
	return 0;
}
