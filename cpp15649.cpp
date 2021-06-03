#include <bits/stdc++.h>

using namespace std;

void swap(int &a, int &b) {
	int temp;
	temp = a;
	a = b;
	b = temp;
}

void permutation(vector<int> v, int depth, int n, int r) {
	if(depth == r) 
	{
		for(int i=0; i<r; i++)
			cout << v[i] << " " ;
		cout << endl;

		return ;
	}

	for(int i = depth; i< n; i++ ) 
	{
		swap(v[depth], v[i]);
		permutation(v, depth+1, n, r);
		swap(v[depth], v[i]);
	}
}

int main() {
	int n, m;
	cin >> n >> m;

	vector<int> v;
	for(int i=1;i<=n;i++ ){
		v.push_back(i);
	}

	permutation(v, 0, n, m);

	return 0;
}
