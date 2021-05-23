#include <bits/stdc++.h>

using namespace std;

char arr[50][50];

int chess(int n, int m) {
	int sw, sb;
	sw = sb = 0;
	
	char swb = 'W';
	for(int i=n; i<n+8; i++ ){
		for(int j=m; j<m+8; j++ ) {
			if(arr[i][j] != swb) {
				sw++;
			}
			if(swb == 'W')
				swb = 'B';
			else
				swb = 'W';
		}
		if(swb == 'W')
			swb = 'B';
		else
			swb = 'W';
	}

	char sbb = 'B';
	for(int i=n; i<n+8; i++ ){
		for(int j=m; j<m+8; j++ ) {
			if(arr[i][j] != sbb) {
				sb++;
			}
			if(swb == 'W')
				sbb = 'B';
			else
				sbb = 'W';
		}
		if(swb == 'W')
			swb = 'B';
		else
			swb = 'W';

	}
	return sw < sb ? sw : sb;
}

int main() {
	int n, m;
	
	cin >> n >> m;
	for(int i = 0 ; i < n; i++ ){
		string a;
		cin >> a;
		for(int j=0; j<a.size(); j++ ){
			arr[i][j] = a[j];
		}
	}

	int ans=2500;
	for(int i=0; i<=(n-8) ; i++ ){
		for(int j = 0 ; j <= (m-8) ; j++ ){
			int temp = chess(i, j);
			ans = ans < temp ? ans : temp;
		}
	}
	cout << ans << endl;	
	return 0;
}
