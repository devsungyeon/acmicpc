#include <bits/stdc++.h>

using namespace std;

int main() {
	int n;
	cin >> n;

	double arr[n];
	double max = 0;
	for(int i = 0 ; i < n ; i++ ) {
		cin >> arr[i];
		if(arr[i] > max)
			max = arr[i];
	}

	for(int i = 0 ; i < n ; i++ ) {
		arr[i] = arr[i] / max * 100;	
	}

	double sum = 0;
	for(int i = 0 ; i < n ; i++ ) {
		sum += arr[i];
	}

	cout << sum / n << endl;

	return 0;
}
