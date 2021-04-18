#include <stdio.h>
#include <string.h>

int main() {
	int n;
	scanf("%d", &n);

	char arr[81];
	for(int i = 0 ; i < n ; i ++ ) {
		int tmp=0, score=0;
		scanf("%s", arr);
		for(int j= 0; j< strlen(arr) ; j++ ) {
			if(arr[j] == 'O') {
				tmp++;
				score+=tmp;
			}
			else {
				tmp=0;
			}
		}
		printf("%d\n", score);
	}
	return 0;
}
