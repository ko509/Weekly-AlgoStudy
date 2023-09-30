import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 시간 : 452ms
// 메모리 : 164048KB
public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
        int[] sum = new int[N + 1];
        int[] remain = new int[M];
		st = new StringTokenizer(br.readLine());
		
		for (int i = 1; i <= N; i++) {
			int n = Integer.parseInt(st.nextToken()) % M;
            sum[i] = (sum[i - 1] + n) % M;
            remain[sum[i]]++;
		}
        
		remain[0]++;
		long total = 0l;
		int prev = 0;
		for (int i = 0; i < N; i++) {
			prev = sum[i];
			remain[prev]--;
			total += remain[prev];
		}
		System.out.println(total);
		
	}

}
