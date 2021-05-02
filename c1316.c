#include <stdio.h>
#include <string.h>
int main() {
	int n, cnt = 0;
	scanf("%d", &n);
	for(int i = 0 ; i < n ; i++) {
		int arr[26] = {0,};
		char str[1000];
		cnt++;
		scanf("%s", str);
		for(int j = 0; j < strlen(str); j++) {
			if(arr[str[j]-97] == 1)
			{
				if (!(str[j] == str[j-1] || str[j] == str[j+1] ))
				{
					cnt--;
					j = 100;
				}
			}	
			else 
				arr[str[j]-97] = 1;	
		}
	}
	printf("%d\n", cnt);
	return 0;
}
