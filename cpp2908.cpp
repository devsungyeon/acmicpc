#include <bits/stdc++.h>

using namespace std;

int main() {
	int a, b;
	cin >> a >> b;

	int ra, rb;
	ra = a/100 + a%100/10*10 + a%10*100;
	rb = b/100 + b%100/10*10 + b%10*100;

	if(ra>rb)
		cout << ra << endl;
	else
		cout << rb << endl;

	return 0;
}
