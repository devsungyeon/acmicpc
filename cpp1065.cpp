#include <bits/stdc++.h>

using namespace std;

int main() {
	int n;
	cin >> n;

	if(n<100) {
		cout << n << endl;
	}
	else {
		int cnt=99;
		for(int i = 100;i<=n;i++) {
			int a = i/100;
			int b = i%100/10;
			int c = i%10;
			if(a-b == b-c)
				cnt++;
		}
		cout << cnt << endl;
	}

	return 0;
}
