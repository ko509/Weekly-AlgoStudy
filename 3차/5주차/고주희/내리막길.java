import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 시간 : 308ms
// 메모리 : 38832KB
public class Main {

	static int N;
	static int M;
	static int[][] map;
	static int[][] cost;
	static boolean[][] v;
	static int[] dr = {-1,0,1,0};
	static int[] dc = {0,-1,0,1};
	
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		map = new int[N][M];
		cost = new int[N][M];
		v = new boolean[N][M];
		cost[0][0] = 1;
		v[0][0] = true;
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		System.out.println(dfs(N - 1, M - 1));
	}
	
	private static int dfs(int r, int c) {
		
		if(v[r][c]) return cost[r][c];
		
		int cnt = 0;
		for (int d = 0; d < 4; d++) {
			int nr = r + dr[d];
			int nc = c + dc[d];
			if(nr >= N || nc >= M || nr < 0 || nc < 0 || map[nr][nc] <= map[r][c]) continue;
			cnt += dfs(nr, nc);
		}
		v[r][c] = true;
		return cost[r][c] = cnt;
	}

}
