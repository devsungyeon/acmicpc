#include <bits/stdc++.h>

using namespace std;

int sang(int i, int n) {
	int temp = i;
	while(i) {
		temp += i%10;
		i /= 10;
	}
	if(temp == n) {
		return 1;
	}
	else {
		return 0;
	}
}

int main() {
	int n;
	cin >> n;
	int ans=0;
	for(int i = 1; i <=n ; i++ ) {
		if(sang(i, n)) {
			ans = i;
			break;
		}
	}
	cout << ans << endl;
	return 0;
}
