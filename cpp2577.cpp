#include <bits/stdc++.h>

using namespace std;

int main() {
	int a, b, c, multi;
	cin >> a >> b >> c;
	multi = a*b*c;

	int arr[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	
	while(multi != 0) {
		int tmp = multi % 10;
		multi = multi / 10;
		arr[tmp]++;
	}

	for(int i = 0 ; i <= 9 ;i++ ) {
		cout <<  arr[i] << endl;;
	}
	return 0;
}
