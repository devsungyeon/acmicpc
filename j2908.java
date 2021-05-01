import java.util.Scanner;
public class j2908 {
	public static void main(String[] args) {
		Scannser sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();

		a = a/100 + a%100/10*10 + a%10*100;
		b = b/100 + b%100/10*10 + b%10*100;

		if(a>b)
			System.out.println(a);
		else
			System.out.println(b);
	}
}
