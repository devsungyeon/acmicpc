#include <iostream>
#include <algorithm>
using namespace std;
#define MOD 1000000

int num[100001], pos[100001];
int n, x, ans;
int pole1, pole2, pole3;

void cal(int n) {
	num[0] = 1;
	for(int i=1; i<=n; i++ )
		num[i] = (num[i-1]*2) % MOD;
}

void hanoi(int disc, int to)
{
	if(disc== 0) return;

	int now = pos[disc];
	int sub;

	for(int i=1; i<=3; i++)
		if(now != i && to != i)
			sub = i;
	if(now == to) hanoi(disc-1, to);
	else
	{
		ans=(ans + num[disc-1]) % MOD;
		hanoi(disc-1, sub);
	}
}

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> n;

	cal(n);

	cin >> pole1 >> pole2 >> pole3 ;

	for(int i=0; i< pole1 ; i++)
	{
		cin >> x;
		pos[x] = 1;
	}
	for(int i=0; i< pole2 ; i++)
	{
		cin >> x;
		pos[x] = 2;
	}
	for(int i=0; i< pole3 ; i++)
	{
		cin >> x;
		pos[x] = 3;
	}

	hanoi(n, pos[n]);

	cout << pos[n] << '\n';
	cout << ans << '\n';

	return 0;
}




