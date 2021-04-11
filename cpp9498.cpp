#include <bits/stdc++.h>

using namespace std;

int main() {
	int score ;
	cin >> score ; 
	score = (int)(score/10);
	char scorec;
	switch (score)
	{
	case 10:
		scorec = 'A';
		break;
	case 9:
		scorec = 'A';
		break;
	case 8:
		scorec = 'B';
		break;
	case 7:
		scorec = 'C';
		break;
	case 6:
		scorec = 'D';
		break;
	default:
		scorec = 'F';
		break;
	}
	cout << scorec << endl;

	return 0;
}
