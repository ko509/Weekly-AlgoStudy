import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

// 시간 : 1260ms
// 메모리 : 97516KB
public class Main {

	static class Node implements Comparable<Node> {
		int h;
		int c;
		
		public Node(int h, int c) {
			super();
			this.h = h;
			this.c = c;
		}
		@Override
		public int compareTo(Node o) {
			int n = this.h - o.h;
			if(n != 0) return n;
			else return o.c - this.c;
		}
		
		
	}
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int S = Integer.parseInt(st.nextToken());
		
		Node[] art = new Node[N];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			
			int H = Integer.parseInt(st.nextToken());
			int C = Integer.parseInt(st.nextToken());
			
			art[i] = new Node(H, C);
		}
		
		Arrays.sort(art);
		
		long[] cost = new long[N];
		cost[0] = art[0].c;
		
		long max = cost[0];
		
		for (int i = 1; i < N; i++) {
			int start = 0;
			int end = i - 1;
			
			while(start <= end) {
				int mid = (start + end) / 2;
				if(art[mid].h < art[i].h - S) {
					start = mid + 1;
				} else if(art[mid].h > art[i].h - S) {
					end = mid - 1;
				} else {
					end = mid;
					break;
				}
			}
			if(end == -1) {
				cost[i] = Math.max(cost[i - 1], art[i].c);
			} else if(art[end].h <= art[i].h - S) {
				cost[i] = cost[end] + art[i].c;
			}
			
			cost[i] = Math.max(cost[i], cost[i-1]);
			max = Math.max(max, cost[i]);
		}
		
		System.out.println(max);
	}

}
