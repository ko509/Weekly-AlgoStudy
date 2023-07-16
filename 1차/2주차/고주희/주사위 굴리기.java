
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 시간 : 88ms
// 메모리 : 11904KB
public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int[] rc = new int[2];
		rc[0] = Integer.parseInt(st.nextToken());
		rc[1] = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		int[][] map = new int[N][M];
		int[] dice = {0, 0, 0, 0, 0, 0}; // 위 아래 북 남 동 서
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		for (int k = 0; k < K; k++) {
			int op = Integer.parseInt(st.nextToken());
			if(move_xy(op, rc, map)) {				
				move_dice(op, dice);
				if(map[rc[0]][rc[1]] == 0) {
					map[rc[0]][rc[1]] = dice[1];
				} else {
					dice[1] = map[rc[0]][rc[1]];
					map[rc[0]][rc[1]] = 0;
				}
				sb.append(dice[0]).append("\n");
			}
		}
		
		System.out.println(sb);
	}


	private static boolean move_xy(int op, int[] rc, int[][] map) {

		int r = rc[0];
		int c = rc[1];
		int N = map.length;
		int M = map[0].length;
		
		if(op == 4) {
			if(r == N - 1) return false;
			else {
				rc[0] += 1;
			}
		} else if(op == 3) {
			if(r == 0) return false;
			else rc[0] -= 1;
		} else if(op == 1) {
			if(c == M - 1) return false;
			else rc[1] += 1;
		} else {
			if(c == 0) return false;
			else rc[1] -= 1;
		}
		return true;
	}


	private static void move_dice(int op, int[] dice) {

		// 주사위는 위 아래 북 남 동 서
		if (op == 1) { // 동쪽으로 이동
			int tmp = dice[0];
			dice[0] = dice[5];
			dice[5] = dice[1];
			dice[1] = dice[4];
			dice[4] = tmp;
		} else if(op == 2) {
			int tmp = dice[0];
			dice[0] = dice[4];
			dice[4] = dice[1];
			dice[1] = dice[5];
			dice[5] = tmp;
		} else if(op == 3) {
			int tmp = dice[0];
			dice[0] = dice[3];
			dice[3] = dice[1];
			dice[1] = dice[2];
			dice[2] = tmp;
		} else {
			int tmp = dice[0];
			dice[0] = dice[2];
			dice[2] = dice[1];
			dice[1] = dice[3];
			dice[3] = tmp;
		}
	}

}
