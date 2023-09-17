import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    static int[][][] dr = {
				{
					{}
				},
				{ 
					{0}, {-1}, {0}, {1}
				},
				{ 
					{0,0}, {1,-1}
				},
				{
					{0,1},{0,1},{0,-1},{0,-1}
				},
				{ 
					{0,-1,0}, {-1,0,1}, {0,1,0}, {1,0,-1}
				},
				{ 
					{0,-1,0,1}
				}
		};
		static int[][][] dc = {
				{
					{}
				},
				{ 
					{-1}, {0}, {1}, {0}
				},
				{ 
					{1,-1}, {0,0}
				},
				{ 
					{1,0},{-1,0},{1,0},{-1,0}
				},
				{ 
					{-1,0,1}, {0,1,0}, {1,0,-1}, {0,-1,0}
				},
				{ 
					{-1,0,1,0}
				}
		};
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		int N = str.charAt(0) - '0';
		int M = str.charAt(2) - '0';
		
		int[][] map = new int[N][M];
		List<int[]> cctv = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			char[] cs = br.readLine().toCharArray();
			for (int j = 0; j < M; j++) {
				map[i][j] = cs[j*2] - '0';
				if(map[i][j] > 0 && map[i][j] < 6) {
					cctv.add(new int[] {i, j, map[i][j]});
				}
			}
		}
		min = Integer.MAX_VALUE;
		watch(0, cctv, map, new boolean[N][M]);
		System.out.println(min);
	}

	static int min;
	private static void watch(int cnt, List<int[]> cctv, int[][] map, boolean[][] v) {

		if(cnt == cctv.size()) {
			int total = 0;
			for (int[] is : map) {
				for (int i : is) {
					if(i == 0) total++;
				}
			}
			min = Math.min(min, total);
			return;
		}
		
		int N = map.length;
		int M = map[0].length;
		int[] cur = cctv.get(cnt);
		int r = cur[0];
		int c = cur[1];
		int dlen = dr[cur[2]].length; 
		for (int i = 0; i < dlen; i++) { 
			int size = dr[cur[2]][0].length;
			for (int d = 0; d < size; d++) { 
				int nr = r;
				int nc = c;
				while(true) {
					if(nr >= N || nc >= M || nr < 0 || nc < 0) break;
					if(map[nr][nc] == 6) break;
					if(map[nr][nc] <= 0) {
						map[nr][nc] -= 1;
					}
					nr += dr[cur[2]][i][d];
					nc += dc[cur[2]][i][d];
				}
			}
			watch(cnt + 1, cctv, map, v);
			for (int d = 0; d < size; d++) {
				int nr = r;
				int nc = c;
				while(true) {
					if(nr >= N || nc >= M || nr < 0 || nc < 0) break;
					if(map[nr][nc] == 6) break;
					if(map[nr][nc] < 0) {
						map[nr][nc] += 1;
					}
					nr += dr[cur[2]][i][d];
					nc += dc[cur[2]][i][d];
				}
			}
		}
	}

}
