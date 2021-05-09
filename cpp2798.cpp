#include <bits/stdc++.h>

using namespace std;

int main() {
	int n, m;
	cin >> n >> m;
	int cards[100];
	for(int i = 0 ; i < n ; i++ ){
		cin >> cards[i];
	}
	vector<int> tmp;
	for(int i = 0 ; i < n ; i++) {
		for(int j = 0 ; j < n ; j++ ) {
			for(int k = 0 ; k < n ; k++ ) {
				if(i == j || j == k || i == k) {

				}
				else {
					tmp.push_back(cards[i] + cards[j] + cards[k]);
				}
			}
		}
	}
	sort(tmp.begin(), tmp.end());
	int ans = tmp[0];
	for(int a : tmp) {
		if(a > m)
			break;
		else
			ans = a;
	}
	cout << ans << endl;

	return 0;
}
