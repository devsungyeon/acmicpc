#include <bits/stdc++.h>

using namespace std;

int main() {
	int n;
	cin >>n ;
	vector<vector<int>> arr(n, vector<int>(2,0));

	for(int i=0;i<arr.size();i++) {
		cin>>arr[i][0];
		cin>>arr[i][1];
	}

	sort(arr.begin(), arr.end());

	for(int i =0 ; i <arr.size(); i++) {
		cout << arr[i][0] << " " << arr[i][1] << '\n';
	}



	/*
	int n;
	cin >> n;

	vector<pair<int, int>> arr;

	for(int i=0;i<n;i++) {
		int a, b;
		cin >> a >> b;
		arr.push_back(make_pair(a,b));
	}

	for(int i=0;i<arr.size();i++) {
		for(int j=i+1;j<arr.size();j++){
			if(arr[i].first > arr[j].first) {
				pair<int, int> temp;
				temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
			else if(arr[i].first == arr[j].first) {
				if(arr[i].second > arr[j].second) {
					pair<int, int> temp;
					temp = arr[i];
					arr[i] = arr[j];
					arr[j] = temp;
				}
			}
		}
	}

	for(pair<int, int> i : arr)
		cout << i.first << " " << i.second << endl;
	*/
	return 0;
}
