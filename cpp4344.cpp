#include <bits/stdc++.h>

using namespace std;

int main() {
	int c;
    cin >> c;
    for(int i = 0 ; i < c ; i++ ) {
        int n;
        cin >> n;
        int arr[1001];
        int sum = 0;
        for(int j = 0 ; j < n ; j++) {
            int tmp;
            cin >> tmp;
            arr[j] = tmp;
            sum += tmp;
        }
        double cnt = 0 ;
        double avg = (double)sum/(double)n;
        for(int j = 0 ; j < n ; j++) {
            if(arr[j] > avg) {
                cnt++;
            }    
        }
        double per = cnt/(double)n*100;
        cout << fixed;
        cout.precision(3);
        cout << per << "%" << endl;
    }
	return 0;
}
