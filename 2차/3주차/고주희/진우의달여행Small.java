import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 시간 : 84ms
// 메모리 : 11776KB
public class Main {

	static class Node {
		int right;
		int straight;
		int left;
		
		public Node(int right, int straight, int left) {
			super();
			this.right = right;
			this.straight = straight;
			this.left = left;
		}
	}
	
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int[][] road = new int[N][M];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				road[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		Node[][] cost = new Node[N][M];
		
		for (int i = 0; i < M; i++) {
			int left = Integer.MAX_VALUE;
			int right = Integer.MAX_VALUE;
			int straight = road[0][i] + road[1][i];
			
			if(i - 1 >= 0) left = road[0][i - 1] + road[1][i];
			if(i + 1 < M) right = road[0][i + 1] + road[1][i];
			
			cost[1][i] = new Node(right, straight, left);
		}
		
		for (int i = 2; i < N; i++) {
			for (int j = 0; j < M; j++) {
				int left = Integer.MAX_VALUE;
				int right = Integer.MAX_VALUE;
				int straight = Integer.MAX_VALUE;
				
				if(j - 1 >= 0) {
					left = road[i][j] + Math.min(cost[i - 1][j - 1].straight, cost[i - 1][j - 1].right);
				}
				
				if(j + 1 < M) {
					right = road[i][j] + Math.min(cost[i - 1][j + 1].left, cost[i - 1][j + 1].straight);
				}
				
				straight = road[i][j] + Math.min(cost[i - 1][j].left, cost[i - 1][j].right);
				
				cost[i][j] = new Node(right, straight, left);
			}
		}
		
		int min = Integer.MAX_VALUE;
		for (int i = 0; i < M; i++) {
			min = Math.min(min, cost[N-1][i].left);
			min = Math.min(min, cost[N-1][i].right);
			min = Math.min(min, cost[N-1][i].straight);
		}
		
		System.out.println(min);
	}

}
