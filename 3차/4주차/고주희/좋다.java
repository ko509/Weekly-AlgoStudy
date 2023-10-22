import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int[] number = new int[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < N; i++) {
			number[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(number);
		
		int cnt = 0;
		for (int i = 0; i < N; i++) {
			int start = 0;
			int end = N - 1;
			
			while(start<end) {
				int add = number[start]+number[end];
				if(add==number[i] && start!=i && end!=i) {
					cnt++;
					break;
				} else if(add==number[i]){
					if(start==i) start++;
					else end--;
				}else if(add > number[i]) end--;
				else start++;
			}
		}
		System.out.println(cnt);
	}

}
