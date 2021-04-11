#include <stdio.h>

int main() {
	int x, y;
	scanf("%d", &x);
	scanf("%d", &y);
	int quadrant ;
	if(x>0 && y>0) {
		quadrant = 1;
	}
	else if(x<0 && y>0) {
		quadrant = 2;
	}
	else if(x<0 && y<0) {
		quadrant = 3;
	}
	else {
		quadrant = 4;
	}
	printf("%d", quadrant);
	return 0;
}
