import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

// 시간 : 100ms
// 메모리 : 12612KB
public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int M = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());
		
		char[][] wall = new char[N][M];
		boolean[][] v = new boolean[N][M];
		
		for (int i = 0; i < N; i++) {
			wall[i] = br.readLine().toCharArray();
		}
		
		PriorityQueue<int[]> que = new PriorityQueue<>(new Comparator<int[]>() {

			@Override
			public int compare(int[] o1, int[] o2) {
				return o1[2] - o2[2];
			}
		});
		
		que.offer(new int[] {0, 0, 1});
		v[0][0] = true;
		
		int[] dr = {-1,0,1,0};
		int[] dc = {0,-1,0,1};
		
		while(!que.isEmpty()) {
			int[] cur = que.poll();
			if(cur[0] == N - 1 && cur[1] == M - 1) {
				System.out.println(cur[2] - 1);
				return;
			}
			
			for (int d = 0; d < 4; d++) {
				int nr = cur[0] + dr[d];
				int nc = cur[1] + dc[d];
				
				if(nr >= N || nc >= M || nr < 0 || nc < 0) continue;
				if(v[nr][nc]) continue;
				if(wall[nr][nc] == '1') {
					v[nr][nc] = true;
					que.offer(new int[] {nr, nc, cur[2] + 1});
				} else {
					v[nr][nc] = true;
					que.offer(new int[] {nr, nc, cur[2]});
				}
			}
		}
		
	}

}
