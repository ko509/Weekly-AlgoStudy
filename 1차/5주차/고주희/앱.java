import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.io.InputStreamReader;

// 시간 : 128ms
// 메모리 : 20176KB
public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		int[] mem = new int[N+1];
		st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= N; i++) {
			mem[i] = Integer.parseInt(st.nextToken());
		}
		
		int[] cost = new int[N+1];
		st = new StringTokenizer(br.readLine());
		int max_cost = 0;
		for (int i = 1; i <= N; i++) {
			cost[i] = Integer.parseInt(st.nextToken());
			max_cost += cost[i];
		}
		
		long[][] ns = new long[N+1][max_cost+1];

		for (int i = 1; i <= N; i++) {
			if(cost[i] == 0) ns[i][0] = ns[i-1][0] + mem[i];
			else ns[i][0] = ns[i-1][0];
		}
		// 행은 메모리, 열은 cost
		int min = 100001;
		for (int i = 1; i <= N; i++) {
			for (int j = 0; j <= max_cost; j++) {
				if(j >= cost[i] && j >= 1) ns[i][j] = Math.max(ns[i-1][j - cost[i]] + mem[i], Math.max(ns[i][j-1], ns[i-1][j]));
				else if(j >= 1) ns[i][j] = Math.max(ns[i][j-1], ns[i-1][j]);
				if(ns[i][j] >= M) min = Math.min(min, j);

			}
		}
		
		System.out.println(min);
	}

}
