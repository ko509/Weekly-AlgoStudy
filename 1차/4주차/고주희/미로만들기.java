import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

// 시간 : 116ms
// 메모리 : 15968KB
public class Main {
	
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		boolean[][] map = new boolean[N][N];
		int[][] cnt_map = new int[N][N];
		
		for (int i = 0; i < N; i++) {
			String str = br.readLine();
			for (int j = 0; j < N; j++) {
				map[i][j] = str.charAt(j) == '0' ? false : true;
				cnt_map[i][j] = Integer.MAX_VALUE;
			}
		}
		
		Queue<int[]> que = new LinkedList<>();
		que.offer(new int[] {0,0,0});
		cnt_map[0][0] = 0;
		
		int[] dr = {-1,0,1,0};
		int[] dc = {0,-1,0,1};
		
		while(!que.isEmpty()) {
			int[] cur = que.poll();
			int r = cur[0];
			int c = cur[1];
			int cnt = cur[2];
			for (int d = 0; d < 4; d++) {
				int nr = r + dr[d];
				int nc = c + dc[d];
				if(nr < 0 || nc < 0 || nr >= N || nc >= N) continue;
				if(!map[nr][nc]) {
					if(cnt_map[nr][nc] > cnt + 1) {
						que.offer(new int[] {nr, nc, cnt + 1});
						cnt_map[nr][nc] = cnt + 1;
					}
				} else {
					if(cnt_map[nr][nc] > cnt) {
						que.offer(new int[] {nr, nc, cnt});
						cnt_map[nr][nc] = cnt;
					}
				}
			}
		}
		
		System.out.println(cnt_map[N-1][N-1]);
	}

}
