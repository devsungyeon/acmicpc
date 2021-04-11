import java.util.Scanner;
public class j2753 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in) ;
		int year = sc.nextInt();
		int yunyear = 0;	
		if(year % 4 == 0 ) {
			if(year % 100 != 0 || year % 400 == 0 ){
				yunyear = 1;
			}
		}
		System.out.println(yunyear);
	}
}
