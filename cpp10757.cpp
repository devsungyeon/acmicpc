#include <bits/stdc++.h>

using namespace std;

int n, sum;
vector<int> num1, num2;
string s1, s2, tmp;
vector<int> ans;

int main() {
	cin >> s1;
	cin >> s2;

	for(char i : s1){
		if(i != '\n')
			num1.push_back((int)(i-'0'));
	}
	for(char i : s2){
		if(i != '\n')
			num2.push_back((int)(i-'0'));
	}

	reverse(num1.begin(), num1.end());
	reverse(num2.begin(), num2.end());

	
	return 0;
}
