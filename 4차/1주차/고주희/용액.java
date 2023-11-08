import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 시간 : 276ms
// 메모리 : 31528KB
public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int[] num = new int[N];
		for (int i = 0; i < N; i++) {
			num[i] = Integer.parseInt(st.nextToken());
		}
		
		if(num[0] >= 0) {
			System.out.println(num[0] + " " + num[1]);
		} else if(num[N - 1] <= 0) {
			System.out.println(num[N - 2] + " " + num[N - 1]);
		} else {
			int start = 0;
			int end = N - 1;
			
			int left = 0;
			int right = N - 1;
			int min = Math.abs(num[start] + num[end]);
			
			while(start < end) {
				int tmp = num[start] + num[end];
				if(Math.abs(tmp) < min) {
					left = start;
					right = end;
                    min = Math.abs(tmp);
				}
				if(tmp == 0) {
					System.out.println(num[start] + " " + num[end]);
					return;
				} else if(tmp < 0) {
					start++;
				} else {
					end--;
				}
			}
			
			System.out.println(num[left] + " " + num[right]);
		}
	}

}
