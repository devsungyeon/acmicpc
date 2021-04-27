#include <stdio.h>
#include <string.h>

int main() {
	int arr[26], i, j;
	char s[100];

	scanf("%s", s);

	for(i = 0 ; i < 26 ; i++ ) arr[i] = -1;

	for(i = 'a'; i<='z';i++ ) {
		for(j = 0 ; j < strlen(s); j++) {
			if(i == s[j]){
				arr[i-'a'] = j;
				break;
			}
		}
	}

	for (i = 0 ; i < 26; i++ ) {
		printf("%d ", arr[i]);
	}

	return 0;
}
