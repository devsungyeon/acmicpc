#include <bits/stdc++.h>

using namespace std;

int main() {
	int year ;
	cin >> year;	
	int yunyear = 0;
	if(year % 4== 0) {
		if(year % 100 != 0 || year % 400 == 0) {
			yunyear = 1;
		}
	}
	cout << yunyear << endl;
	return 0;
}
