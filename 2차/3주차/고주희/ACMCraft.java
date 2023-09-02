import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

// 시간 : 1072ms
// 메모리 : 249424KB
public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		
		while(--T >= 0) {
			st = new StringTokenizer(br.readLine());
			
			int N = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());
			
			int[] cost = new int[N];
			int[] prev = new int[N];
			List<Integer>[] list = new ArrayList[N];
			
			
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < cost.length; i++) {
				cost[i] = Integer.parseInt(st.nextToken());
				list[i] = new ArrayList<>();
			}
			
			
			for (int i = 0; i < K; i++) {
				st = new StringTokenizer(br.readLine());
				int start = Integer.parseInt(st.nextToken()) - 1;
				int end = Integer.parseInt(st.nextToken()) - 1;
				
				list[start].add(end);
				prev[end]++;
			}
			
			int W = Integer.parseInt(br.readLine()) - 1;
			
			Queue<int[]> que = new LinkedList<>();
			for (int i = 0; i < N; i++) {
				if(prev[i] == 0) que.offer(new int[] {i, 0});
			}
			
			int time = 0;
			int[] max = new int[N];
			
			while(!que.isEmpty()) {
				int[] cur = que.poll();
				int n = cur[0];
				int t = cur[1];
				
				
				if(n == W) {
					time = cost[n] + t;
					break;
				}
				
				for (int i : list[n]) {
					prev[i]--;
					if(max[i] < cost[n] + t) {
						max[i] = cost[n] + t;
					}
					if(prev[i] == 0) {
						que.offer(new int[] {i, max[i]});
					}
				}
			}
			
			System.out.println(time);
		}
	}

}
