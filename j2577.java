import java.util.Scanner;
public class j2577 {
	public static void main(String[] args) {
		Scanner sc =  new Scanner(System.in);
		int a, b, c, multi;
		a = sc.nextInt();
		b = sc.nextInt();
		c = sc.nextInt();
		multi = a*b*c;

		int[] arr = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		
		while(multi != 0) {
			int tmp = multi % 10;
			multi = multi / 10;
			arr[tmp]++;
		}

		for(int i = 0 ; i <= 9 ;i++ ) {
			System.out.println(arr[i]);
		}
		
	}
}
