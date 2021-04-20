import java.util.Scanner;
public class j4344 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
        int c = sc.nextInt();
        for(int i = 0 ; i < c ; i++ ) {
            int arr[] = new int[1001];
            int n = sc.nextInt();
            int sum = 0;
            for(int j = 0 ; j < n ; j++ ) {
                int tmp = sc.nextInt();
                sum += tmp;
                arr[j] = tmp;
            }
            
            float avg = (float)sum / (float)n;    
            int cnt = 0;
            for(int j = 0 ; j < n ; j++ ) {
                if((float)arr[j] > avg)
                    cnt++;
            }
            
            float per = cnt / (float)n * 100;
            System.out.println(String.format("%.3f", per) + "%");
            
        }
	}
}
