#include <bits/stdc++.h>

using namespace std;

int main() {
	int n;
	cin >> n;
	int min, max;
	min = 1000001;
	max = -1000001;

	int input;
	for(int i = 0 ; i < n ;i ++ ) {
		cin >> input;
		if(input > max)
			max = input;
		if(input < min)
			min = input;
	}
	cout << min << " " << max ;
	
	return 0;
}
