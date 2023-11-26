import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 시간 : 128ms
// 메모리 : 12380KB
public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[] num = new int[N + 2];
		int[] increase = new int[N + 1];
		int[] decrease = new int[N + 2];
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for (int i = 1; i <= N; i++) {
			num[i] = Integer.parseInt(st.nextToken());
		}
		
		for (int i = 1; i <= N; i++) {
			for (int j = 0; j < i; j++) {
				if(num[i] > num[j]) {
					if(increase[j] + 1 > increase[i]) increase[i] = increase[j] + 1;
				}
			}
		}
		
		int max = 0;
		for (int i = N + 1; i >= 0; i--) {
			for (int j = N + 1; j > i; j--) {
				if(num[i] > num[j]) {
					if(decrease[j] + 1 > decrease[i]) decrease[i] = decrease[j] + 1;
				}
			}
			
		}
		
		for (int i = 1; i <= N; i++) {
			if(max < increase[i] + decrease[i] - 1) {
				max = increase[i] + decrease[i] - 1;
			}
		}
		
		System.out.println(max);
	}

}
