#include <bits/stdc++.h>

using namespace std;

int main() {
	int n;
	cin >> n;
	int ans = n;
	for(int i = 0 ; i < n ; i++ ) {
		int t;
		cin >> t;
		if(t == 1)
			ans--;
		for(int j = 2 ; j <= sqrt(t) ; j++ ) {
			if(t % j == 0 ) {
				ans--;
				break;
			}
		}
	}
	
	cout << ans << endl;

	return 0;
}
