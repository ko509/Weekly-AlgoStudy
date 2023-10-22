import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static class Move{
		int r;
		int c;
		int cnt;
		int breakWall;
		
		public Move (int r, int c) {
			this.r = r;
			this.c = c;
			this.cnt = 1;
			this.breakWall = 0;
		}
		
		public Move (int r, int c, int cnt, int breakWall) {
			this.r = r;
			this.c = c;
			this.cnt = cnt;
			this.breakWall = breakWall;
		}
		
	}
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		char[][] map = new char[N][M];
		for (int i = 0; i < N; i++) {
			map[i] = br.readLine().toCharArray();
		}

		Queue<Move> que = new LinkedList<>();
		que.offer(new Move(0, 0));
		int[][][] v = new int[N][M][2];
		v[0][0][0] = 1; // 0은 안부순거, 1은 부순거
		for(int[][] is : v) {
            for(int[] iss : is) {
                Arrays.fill(iss, Integer.MAX_VALUE);
            }
        }
		int[] dr = {-1,0,1,0};
		int[] dc = {0,-1,0,1};
		
		int answer = -1;
		while(!que.isEmpty()) {
			Move cur = que.poll();
			if(cur.r==N-1 && cur.c==M-1) {
				answer = cur.cnt;
				break;
			}
			for (int d = 0; d < 4; d++) {
				int nr = cur.r + dr[d];
				int nc = cur.c + dc[d];
				if(nr >= N || nc >= M || nr < 0 || nc < 0) {
					continue;
				}
				if(v[nr][nc][cur.breakWall] <= cur.cnt) {
					continue;
				}
				if(map[nr][nc]=='1' && cur.breakWall==0) {
					v[nr][nc][1] = cur.cnt;
					que.offer(new Move(nr, nc, cur.cnt+1, 1));
				} else if(map[nr][nc]=='0') {
					v[nr][nc][cur.breakWall] = cur.cnt;
					que.offer(new Move(nr, nc, cur.cnt+1, cur.breakWall));
				} 
			}
		}
		System.out.println(answer);
	}

}
