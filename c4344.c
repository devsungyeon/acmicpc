#include <stdio.h>

int main() {
	int c;
    scanf("%d", &c);
    
    int arr[1001];
    
    for(int i = 0 ; i < c ; i++ ) {
        int n;
        scanf("%d", &n);
        int sum=0;
        double avg;
        for(int j = 0 ; j < n ; j++ ) {
            int tmp ;
            scanf("%d", &tmp);
            arr[j] = tmp;
            sum += tmp;
        }
        avg = sum / n;
        
        double cnt=0;
        for(int j = 0 ; j < n ; j++ ) {
            if(arr[j] > avg)
                cnt++;
        }
        printf("%.3lf%%\n", (cnt*100)/(double)n);
    }
    
	return 0;
}
