#include <bits/stdc++.h>

using namespace std;

int arr[10001];
void selfnum(int a) {
	if(a > 10000)
		return;
	int sum = a;
	while(a) {
		sum += a%10;
		a = a/10;
	}
	arr[sum] = 0;
	selfnum(sum);
}

int main() {
	std::fill_n(arr, 10001, 1);
	for(int i = 1; i<= 10000; i++ ) 
		if(arr[i] == 1) 
			selfnum(i);

	for(int i = 1; i<= 10000; i++ )
		if(arr[i] == 1)
			cout << i << endl;
	
	return 0;
}
