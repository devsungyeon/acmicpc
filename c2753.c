#include <stdio.h>

int main() {
	int year;
	scanf("%d", &year);
	int yunyear=0;
	if(year % 4 == 0) {
		if(year % 100 != 0 || year % 400 == 0 )
			yunyear = 1;
	}
	printf("%d\n", yunyear);
	return 0;
}
