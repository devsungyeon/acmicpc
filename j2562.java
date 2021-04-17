import java.util.Scanner;
public class j2562 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int max, idx;
		max = 0;
		for (int i = 1 ; i <= 9 ; i++ ) {
			int tmp = sc.nextInt();
			if(tmp > max) {
				max = tmp;
				idx = i;
			}
		}
		System.out.println(max);
		System.out.println(idx);
	}
}
