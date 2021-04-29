#include <bits/stdc++.h>
#define MAX 1000001
using namespace std;

int main() {
	char str[MAX];
	int i;
	int num[26] = {0,};
	int max;
	int max_index = 0;

	cin >> str;

	for(i = 0; str[i] != '\0'; i++) {
		if(str[i] < 97)
			str[i] += 32;
		num[str[i] - 97]++;
	}
	max = num[0];
	for(i = 1 ; i<26; i++ ) {
		if(max < num[i]) {
			max = num[i];
			max_index = i;
		}
		else if(max == num[i] && num[i] != 0) {
			max_index = -1;
		}
	}
	if(max_index != -1)
		 cout << char(65+max_index);
	else
		cout << "?\n";

	return 0;
}
