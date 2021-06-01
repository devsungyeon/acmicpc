#include <bits/stdc++.h>
#define N 100000000
using namespace std;

int ans = 0;
vector<pair<int, int>> a;

void hanoi(int n, int f, int by, int t) {
	if(n==1)
	{
		a.push_back(make_pair(f, t));
		ans++;
	}
	else
	{
		hanoi(n-1, f, t, by);
		a.push_back(make_pair(f, t));
		ans++;
		hanoi(n-1, by, f, t);
	}
}

int main() {
	int n;
	cin >> n;
	
	hanoi(n, 1, 2, 3);

	cout << ans << endl;
	for(pair<int, int> i : a) {
		cout << i.first << " " << i.second << endl;
	}

	return 0;
}
