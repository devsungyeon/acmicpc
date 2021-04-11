import java.util.Scanner;
public class j9498 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int score = sc.nextInt();
		score = (int)(score/10);
		char scorec;
		switch (score) {
			case 10:
				scorec = 'A';	
				break;
			case 9:
				scorec = 'A';	
				break;
			case 8:
				scorec = 'B';	
				break;
			case 7:
				scorec = 'C';	
				break;
			case 6:
				scorec = 'D';	
				break;
			default:
				scorec = 'F';
				break;
		}
		System.out.println(scorec);
	}
}
