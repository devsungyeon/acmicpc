#include <bits/stdc++.h>

using namespace std;

int main() {
	int t;
	cin >> t;
	while(t-->0) {
		int arr[15] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14};
		int k, n;
		cin >> k;
		cin >> n;
		for(int i = 0 ; i < k ; i++ ) {
			for(int j = 1; j <= n; j++ ) {
				arr[j] += arr[j-1];
			}
		}
		cout << arr[n] << endl;
	}
	return 0;
}
