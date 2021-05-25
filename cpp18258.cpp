#include <bits/stdc++.h>

using namespace std;

int main() {
	int n, k;
	cin >> n >> k;
	vector<int> arr;
	for(int i=0; i<n ;i++ ){
		int tmp;
		cin >> tmp;
		arr.push_back(tmp);
	}
	reverse(arr.begin(), arr.end());
	int ans =0;
	for(auto i : arr)
	{
		if(k / i >  0) {
			ans += k / i;
			k = k % i;
		}
	}
	cout << ans << endl;
	return 0;
}
