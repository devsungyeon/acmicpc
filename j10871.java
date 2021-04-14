import java.util.Scanner;
public class j10871 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int x = sc.nextInt();
		int input;
		for(int i=0; i<n; i++ ){
			input = sc.nextInt();
			if(x> input)
				System.out.print(input + " ") ;
		}
	}
}
