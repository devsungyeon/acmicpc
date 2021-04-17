#include <bits/stdc++.h>

using namespace std;

int main() {
	int arr[42] = {0,};
	int tmp, ans=0;
	for(int i = 0 ; i < 10 ; i++ ) {
		cin >> tmp;
		arr[tmp % 42]++;
	}
	for(int i = 0 ; i < 42; i++ ) {
		if(arr[i] != 0)
			ans++;
	}
	cout << ans;
	return 0;
}
