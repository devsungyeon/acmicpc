#include <stdio.h>

int main() {
	char num; int dial;
	while( (num = getchar()) - 0x0A) {
		for( char c : "zzADGJMPTW")
			dial += num >= c;
		dial++;

	}
	printf("%d\n", dial);
	return 0;

}
