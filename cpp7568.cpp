#include <bits/stdc++.h>

using namespace std;

int main() {
	int n;
	cin >> n;
	int arr[3][50];
	for(int i = 0 ; i < n ; i++ ) {
		cin >> arr[0][i] >> arr[1][i];
		arr[2][i] = 1;
	}
	for(int i = 0 ; i < n ; i++ ) {
		for(int j = i+1 ; j< n;j++ ){
			if(arr[0][i] < arr[0][j] && arr[1][i] < arr[1][j])
				arr[2][i]++;
			
			if(arr[0][i] > arr[0][j] && arr[1][i] > arr[1][j])
				arr[2][j]++;
		}
	}

	for(int i = 0 ; i < n ; i++ )
		cout << arr[2][i] << " " ;
	return 0;
}
