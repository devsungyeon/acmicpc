#include <bits/stdc++.h>

using namespace std;

int main() {
	int n;
	cin >> n;
	int arr[10000001] ;
	for(int i=1;i<10000001;i++)
	{
		arr[i] = 0;
	}
	for(int i = 0 ; i<n; i++)
	{
		int temp;
		cin >> temp;
		arr[temp]++;
	}
	cout << "test" << endl;
	/*
	for(int i=1;i<10000001;i++)
	{
		if(arr[i] != 0)
		{
			for(int j=0;j<arr[i];j++)
				cout << i << endl;
		}
	}
*/
	return 0;
}
