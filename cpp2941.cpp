#include <bits/stdc++.h>

using namespace std;

int main() {
	char arr[100];
	cin >> arr;

	int sum = strlen(arr);
	for(int j = 0 ; j<strlen(arr); j++ ) {
		if((arr[j] == 'l' || arr[j] == 'n') && arr[j+1] == 'j')
			sum--;
		if(arr[j] == 'd' && arr[j+1] == 'z' && arr[j+2] == '=')
			sum--;	
		if(arr[j] == '=' || arr[j] == '-')
			sum--;
	}
	cout << sum;
	return 0;
}
