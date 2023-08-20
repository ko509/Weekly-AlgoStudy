import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

	static class Node implements Comparable<Node>{
		int loc;
		int len;
		public Node(int loc, int len) {
			super();
			this.loc = loc;
			this.len = len;
		}
		
		@Override
		public int compareTo(Node o) {
			return this.loc - o.loc;
		}
		
		
	}
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		
		Node[] arr = new Node[N];
		
		int max = 0;
		int max_loc = -1;
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int loc = Integer.parseInt(st.nextToken());
			int len = Integer.parseInt(st.nextToken());
			
			if(max < len) {
				max = len;
				max_loc = loc;
			}
			
			arr[i] = new Node(loc, len);
		}
		
		Arrays.sort(arr);
		
		int h = arr[0].len;
		int past = arr[0].loc;
		int size = 0;
		for (int i = 1; i < N; i++) {
			if(arr[i].loc == max_loc) break;
			if(arr[i].len > h) {
				size += (arr[i].loc - past) * h;
				h = arr[i].len;
				past = arr[i].loc;
			}
		}
		
		size += (max_loc - past) * h;
		
		h = arr[N-1].len;
		past = arr[N-1].loc + 1;
		
		for (int i = N - 2; i >= 0; i--) {
			if(arr[i].loc == max_loc) break;
			if(arr[i].len > h) {
				size += (past - arr[i].loc - 1) * h;
				h = arr[i].len;
				past = arr[i].loc + 1;
			}
		}
		size += (past - max_loc - 1) * h;
		size += max;
		
		System.out.println(size);
	}

}
