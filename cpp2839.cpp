#include <bits/stdc++.h>

using namespace std;

int main() {
	int n;
	cin >> n;
	int ans = 5000;
	for(int i = 0 ; i <= 1000 ; i++ ) {
		int temp = n;
		temp -= i*5;
		if(temp < 0)
			break;
		int divi = temp / 3;
		int mod = temp % 3;
		if(mod == 0)
			if(ans > divi+i )
				ans = divi + i;
	}
	if(ans==5000)
		cout << -1 << endl;
	else
		cout << ans << endl;
	return 0;
}
