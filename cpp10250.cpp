#include <bits/stdc++.h>

using namespace std;

int main() {
	int t;
	cin >> t ;
	for(int i = 0 ; i < t; i++ ) {
		int h, w, n;
		cin >> h >> w >> n;
		cout << (n-1)%h+1 << std::setw(2) << std::setfill('0') << std::internal << ((n-1)/h+1) << endl;
	}
	return 0;
}
