import java.util.Scanner;

public class j1065 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();

		if(n < 100) {
			System.out.println(n);
		}
		else {
			int cnt = 99;
			for(int i = 100;i<=n;i++ ) {
				int a = i/100;
				int b = (i%100)/10;
				int c = i%10;
				if(a-b == b-c)
					cnt++;
			}
			System.out.println(cnt);
		}
	}
}
