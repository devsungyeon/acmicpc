#include <bits/stdc++.h>

using namespace std;

int main() {
	int k;
	cin >> k;
	
	vector<int> arr;
	for(int i = 0 ; i < k ; i++ )
	{
		int temp;
		cin >> temp;
		if(temp == 0)
			arr.pop_back();
		else
			arr.push_back(temp);
	}
	int ans=0;
	for(auto i : arr)
		ans += i;
	cout << ans << endl;

	return 0;
}
