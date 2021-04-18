import java.util.Scanner;
public class j8958 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String[] arr = new String[n+1];
		for(int i = 0 ; i < n ; i ++ ) {
			int tmp=0, score=0;
			arr[i] = sc.next();
			for(int j= 0; j< arr[i].length() ; j++ ) {
				if(arr[i].charAt(j) == 'O') {
					tmp++;
					score+=tmp;
				}
				else {
					tmp=0;
				}
			}
			System.out.println(score);
		}
	}
}
