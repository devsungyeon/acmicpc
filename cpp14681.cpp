#include <bits/stdc++.h>

using namespace std;

int main() {
	int x, y;
	cin >> x;
	cin >> y;
	int quadrant ;
	if(x>0 && y>0) {
		quadrant = 1;
	}
	else if(x<0 && y>0) {
		quadrant = 2;
	}
	else if(x<0 && y<0) {
		quadrant = 3;
	}
	else {
		quadrant = 4;
	}
	cout << quadrant << endl;
	return 0;
}
