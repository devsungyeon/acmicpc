import java.util.Scanner;
public class j2884 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int h = sc.nextInt();
		int m = sc.nextInt();
		if(m < 45) {
			h += 23;
			h %= 24;
		}
		m += 15;
		m %= 60;
		System.out.println(h + " "+ m);
	}
}
