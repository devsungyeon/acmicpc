#include <bits/stdc++.h>

using namespace std;

long long sum(std::vector<int> &a) {
	long long ret = 0;
	
	for(int i = 0 ; i < a.size() ; i++ ) {
		ret += a[i];
	}

	return ret;
}

int main() {
	vector<int> arr;
	for(int i = 1 ; i <= 10; i++ ) {
		arr.push_back(i);
	}

	int answer = 0;
	answer = sum(arr);
	
	cout << answer << endl;


	return 0;
}
