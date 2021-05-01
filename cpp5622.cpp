#include <bits/stdc++.h>

using namespace std;

int main() {
	char num; int dial;

	while ( (num = getchar()) - 0x0A ) {
		for(char c : "zzADGJMPTW" )
			dial += num >= c;
		dial++;

	}
	cout << dial << endl;
	return 0;
}
