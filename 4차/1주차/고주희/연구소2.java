import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;

// 시간 : 204ms
// 메모리 : 43508KB
public class Main {

	static int N;
	static int M;
	static int[][] map;
	static List<int[]> virus;
	static int size;
	static int[] dr = {-1,0,1,0};
	static int[] dc = {0,-1,0,1};
	static int zero = 0;
	static int min;
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		map = new int[N][N];
		virus = new ArrayList<>();
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				if(map[i][j] == 2) {
					virus.add(new int[] {i, j});
				} else if(map[i][j] == 0) {
					zero++;
				}
			}
		}
		size = virus.size();
		zero += size;
		min = Integer.MAX_VALUE;
		
		comb(0, 0, new int[M]);
		if(min == Integer.MAX_VALUE) System.out.println(-1);
		else System.out.println(min);
	}
	
	private static void comb(int cnt, int start, int[] select) {
		
		if(cnt == M) {
			boolean[][] v = new boolean[N][N];
			Queue<int[]> que = new LinkedList<>();
			
			for (int i = 0; i < M; i++) {
				int[] tmp = virus.get(select[i]);
				que.offer(new int[] {tmp[0], tmp[1], 0});
				v[tmp[0]][tmp[1]] = true;
			}
			
			int time = 0;
			int zone = 0;
			while(!que.isEmpty()) {
				int[] cur = que.poll();
				time = cur[2];
				zone++;
				
				for (int d = 0; d < 4; d++) {
					int nr = cur[0] + dr[d];
					int nc = cur[1] + dc[d];
					if(nr >= N || nc >= N || nr < 0 || nc < 0 || map[nr][nc] == 1 || v[nr][nc]) continue;
					v[nr][nc] = true;
					que.offer(new int[] {nr, nc, cur[2] + 1});
				}
			}
			
			if(zone == zero && min > time) {
				min = time;
			}
			return;
		}
		
		for (int i = start; i < size; i++) {
			select[cnt] = i;
			comb(cnt + 1, i + 1, select);
		}
	}

}
