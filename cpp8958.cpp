#include <bits/stdc++.h>

using namespace std;

int main() {
	int n;
	cin >> n;

	char arr[81];
	for(int i = 0 ; i < n ; i ++ ) {
		int tmp=0, score=0;
		cin >> arr;
		for(int j= 0; j< strlen(arr) ; j++ ) {
			if(arr[j] == 'O') {
				tmp++;
				score+=tmp;
			}
			else {
				tmp=0;
			}
		}
		cout << score << endl;
	}
	return 0;
}
