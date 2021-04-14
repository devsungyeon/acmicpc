import java.util.Scanner;
public class j1110 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int c = 0;
		int result = n;
	
		while(true) {
			c++;
			int t, y;
			t = n / 10;
			y = n % 10;
			n = y*10 + (t+y) % 10;
			if(result == n)
				break;
		}
		System.out.println(c);
	}
}
