#include <bits/stdc++.h>

using namespace std;

int main() {
	vector<int> arr;
	int n;
	cin >> n;
	for(int i=0; i<n;i++) {
		int temp;
		cin >> temp;
		arr.push_back(temp);
	}
	sort(arr.begin(), arr.end());
	for(int i=0; i<n;i++) {
		cout << arr[i] << endl;
	}
	
	return 0;
}
