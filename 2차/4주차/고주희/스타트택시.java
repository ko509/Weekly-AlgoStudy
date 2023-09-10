import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// 시간 : 148ms
// 메모리 : 19676KB
public class Main {

	static int[] dr = {-1,0,1,0};
	static int[] dc = {0,-1,0,1};
	
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int[] bj = new int[3];
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		bj[2] = Integer.parseInt(st.nextToken());
		
		boolean[][] map = new boolean[N][N];
		
		for (int i = 0; i < N; i++) {
			String str = br.readLine();
			for (int j = 0; j < N; j++) {
				map[i][j] = str.charAt(j * 2) == '0' ? true : false;
			}
		}
		
		st = new StringTokenizer(br.readLine());
		int r = Integer.parseInt(st.nextToken()) - 1;
		int c = Integer.parseInt(st.nextToken()) - 1;
		
		bj[0] = r;
		bj[1] = c;
		
		int[][] start = new int[N][N];
		int[][] end = new int[M + 1][2];
		
		for (int i = 1; i <= M; i++) {
			st = new StringTokenizer(br.readLine());
			int sr = Integer.parseInt(st.nextToken()) - 1;
			int sc = Integer.parseInt(st.nextToken()) - 1;
			int er = Integer.parseInt(st.nextToken()) - 1;
			int ec = Integer.parseInt(st.nextToken()) - 1;
			
			start[sr][sc] = i;
			end[i][0] = er;
			end[i][1] = ec;
		}
		
		
		while(M > 0) {
			find_start(start, end, map, bj);
			if(bj[0] == -1) {
				System.out.println(-1);
				return;
			}
			M--;
		}
		
		System.out.println(bj[2]);
	}

	private static void find_start(int[][] start, int[][] end, boolean[][] map, int[] bj) {

		int N = map.length;
		boolean[][] v = new boolean[N][N];
		
		Queue<int[]> que = new LinkedList<>();
		que.offer(new int[] {bj[0], bj[1], 0});
		v[bj[0]][bj[1]] = true;
		
		int r = -1;
		int c = -1;
		int k = Integer.MAX_VALUE;
		
		while(!que.isEmpty()) {
			int[] cur = que.poll();
			if(cur[2] > bj[2]) continue;
			
			if(start[cur[0]][cur[1]] != 0) {
				if(k > cur[2]) {
					r = cur[0];
					c = cur[1];
					k = cur[2];
				} else if(k == cur[2]) {
					if(r > cur[0]) {
						r = cur[0];
						c = cur[1];
					} else if(r == cur[0]) {
						if(c > cur[1]) {
							c = cur[1];
						}
					}
				}
				continue;
			}
			
			if(cur[2] >= k) continue;
			
			for (int d = 0; d < 4; d++) {
				int nr = cur[0] + dr[d];
				int nc = cur[1] + dc[d];
				
				if(nr >= N || nc >= N || nr < 0 || nc < 0 || !map[nr][nc]) continue;
				if(v[nr][nc]) continue;
				
				v[nr][nc] = true;
				que.offer(new int[] {nr, nc, cur[2] + 1});
			}
		}
		
		if(r == -1) {
			bj[0] = -1;
			return;
		}
		
		bj[0] = r;
		bj[1] = c;
		bj[2] -= k;
		if(bj[2] < 0) {
			bj[0] = -1;
			return;
		}
		
		int stand = start[r][c];
		
		start[r][c] = 0;
		
		que = new LinkedList<>();
		que.offer(new int[] {bj[0], bj[1], 0});
		
		v = new boolean[N][N];
		v[bj[0]][bj[1]] = true;
		
		while(!que.isEmpty()) {
			int[] cur = que.poll();
			
			if(end[stand][0] == cur[0] && end[stand][1] == cur[1]) {
				if(cur[2] <= bj[2]) {					
					bj[0] = cur[0];
					bj[1] = cur[1];
					bj[2] += cur[2];
					return;
				} else {
					bj[0] = -1;
					return;
				}
			}
			
			if(cur[2] > bj[2]) {
				bj[0] = -1;
				return;
			}
			
			for (int d = 0; d < 4; d++) {
				int nr = cur[0] + dr[d];
				int nc = cur[1] + dc[d];
				
				if(nr >= N || nc >= N || nr < 0 || nc < 0 || !map[nr][nc]) continue;
				if(v[nr][nc]) continue;
				
				v[nr][nc] = true;
				que.offer(new int[] {nr, nc, cur[2] + 1});
			}
		}
		if(bj[0] != end[stand][0] || bj[1] != end[stand][1]) {
			bj[0] = -1;
			return;
		}
	}

	
}
