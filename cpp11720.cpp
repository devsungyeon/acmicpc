#include <bits/stdc++.h>

#define MAX 100

using namespace std;

int main() {
	int n ; 
	cin >> n;
	string arr;
	cin >> arr;

	int sum = 0 ;
	for (int i = 0 ; i < n ; i++ ) {
		sum += (arr[i]-'0');
	}
	cout << sum << endl;
	return 0;
}
