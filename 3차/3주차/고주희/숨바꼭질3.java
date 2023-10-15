import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		if(N > K) {
			System.out.println(N - K);
			return;
		}
		
		PriorityQueue<int[]> que = new PriorityQueue<>(new Comparator<int[]>() {
			@Override
			public int compare(int[] o1, int[] o2) {
				return o1[1] - o2[1];
			}
			
		});
		int[] v = new int[200001];
		int min = K - N;
		Arrays.fill(v, min);
		que.offer(new int[] {N, 0});
		v[N] = 0;
		
		while(!que.isEmpty()) {
			int[] cur = que.poll();
			if(min <= cur[1]) continue;
			if(cur[0] == K) {
				min = cur[1];
				break;
			}
			
			if(cur[0] < K) {
				if(v[cur[0] * 2] > cur[1]) {					
					que.offer(new int[] {cur[0] * 2, cur[1]});
					v[cur[0] * 2] = cur[1];
				}
				if(v[cur[0] + 1] > cur[1]) {
					que.offer(new int[] {cur[0] + 1, cur[1] + 1});
					v[cur[0] + 1] = cur[1] + 1;
				}
			}
			if(cur[0] > 0 && v[cur[0] - 1] > cur[1]) {
				que.offer(new int[] {cur[0] - 1, cur[1] + 1});
				v[cur[0] - 1] = cur[1] + 1;
			}
		}
		
		System.out.println(min);
	}

}
