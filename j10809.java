import java.util.Scanner;
public class j10809 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		String alphabet = "abcdefghijklmnopqrstuvwxyz";
		for(int i = 0 ; i < alphabet.length(); i++ ) {
			System.out.print(s.indexOf(i+'a') + " ") ;
		}
	}
}
