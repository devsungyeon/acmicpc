#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);
	
	if(n<100){
		printf("%d", n);
	}
	else {
		int cnt=99;
		for(int i = 100;i<=n;i++) {
			int a = i/100;
			int b = i%100/10;
			int c = i%10;
			if(a-b == b-c)
				cnt++;
		}
		printf("%d", cnt);
	}

	return 0;
}
