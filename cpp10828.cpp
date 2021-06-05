#include <bits/stdc++.h>

using namespace std;

vector<int> arr;

int main() {
	int n;
	cin >> n;
	
	for(int i=0;i<n;i++) {
		string s;
		int x;
		cin >> s;

		if(s == "push") {
			cin >> x;			
		}
		
		if(s=="push")
			arr.push_back(x);
		else if(s=="pop")
		{
			if(arr.size() == 0)
				cout << -1 << "\n";
			else {
				cout << arr.back() << "\n";
				arr.pop_back();
			}
		}
		else if(s=="size")
			cout << arr.size() << "\n";
		else if(s=="empty") {
			if(arr.size() == 0)
				cout << 1 << "\n";
			else
				cout << 0 << "\n";
		}
		else if(s=="top")
		{
			if(arr.size()==0)
				cout << -1 << "\n";
			else
				cout << arr.back() << "\n";
		}
			
	}

	return 0;
}
