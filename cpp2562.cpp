#include <bits/stdc++.h>

using namespace std;

int main() {
	int max, tmp, idx;
	max = 0;
	tmp = 0;
	for(int i = 1 ; i<=9; i++ ) {
		cin >> tmp;
		if(tmp > max) {
			max = tmp;
			idx = i;
		}
	}
	cout << max << endl << idx ;
	return 0;
}
