import java.util.Scanner;
import java.util.*;
public class j4673 {
	static int[] arr = new int[10010];
	static void selfnum(int a) {
		if(a > 10000)
			return;
		int sum = a;
		while(a>0) {
			sum += a%10;
			a = a/10;
		}
		if(sum < 10001)
			arr[sum] = 0;
		selfnum(sum);
	}
	public static void main(String[] args) {
		for(int i = 1; i<= 10000; i++ ) 
			arr[i] = 1;
		for(int i = 1; i<= 10000; i++ ) 
			if(arr[i] == 1) 
				selfnum(i);
	
		for(int i = 1; i<= 10000; i++ )
			if(arr[i] == 1)
				System.out.println(i);
	}
}
