#include <bits/stdc++.h>

using namespace std;

int main() {
	int n;
	cin >> n;
	int f, t;
	f = n/5;
	n -= f*5;
	t = n/3;
	n -= t*3;
	if(n==0)
		cout << f+t << endl;
	else
		cout << -1 << endl;
	return 0;
}
