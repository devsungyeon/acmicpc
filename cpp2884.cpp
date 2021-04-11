#include <bits/stdc++.h>

using namespace std;

int main() {
	int h, m;
	cin >> h >> m;
	if(m < 45) {
		h += 23;
		h %= 24;
	}
	m += 15;
	m %= 60;
	
	cout << h << " " << m << endl;
	return 0;
}
