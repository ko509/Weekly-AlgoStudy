import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 시간 : 240ms
// 메모리 : 27636KB
public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int H = Integer.parseInt(st.nextToken());
		
		int[] sum = new int[H];
		for (int i = 0; i < N; i++) {
			int n = Integer.parseInt(br.readLine());
			
			if(i % 2 == 0) { // 석순
				sum[0]++;
				sum[n]--;
			} else {
				sum[H - n]++;
			}
		}
		
		
		int cnt = 1;
		int min = sum[0];
		for (int i = 1; i < H; i++) {
			sum[i] += sum[i-1];
			if(sum[i] < min) {
				min = sum[i];
				cnt = 1;
			} else if(sum[i] == min) {
				cnt++;
			}
		}
		
		System.out.println(min + " " + cnt);
	}

}
