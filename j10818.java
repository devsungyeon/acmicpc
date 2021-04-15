import java.util.Scanner;
public class j10818 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int min, max;
		min = 1000001;
		max = -1000001;
		int input;
		for(int i =0 ; i < n ; i ++ ) {
			input = sc.nextInt();
			if(input > max)
				max = input;
			if(input < min)
				min = input;
		}
		System.out.println(min + " " + max);
	}
}
