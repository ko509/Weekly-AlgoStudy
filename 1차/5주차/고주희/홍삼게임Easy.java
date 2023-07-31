import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// 시간 : 192ms
// 메모리 : 43152KB
public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int A = Integer.parseInt(st.nextToken()) - 1; // 첫번째 지목
		int B = Integer.parseInt(st.nextToken()) - 1; // 두번째 지목
		int DA = Integer.parseInt(st.nextToken());
		int DB = Integer.parseInt(st.nextToken());
		
		int[][][] map = new int[2][N][N];
		
		Queue<int[]> que = new LinkedList<>();
		
		que.offer(new int[] {A, B, 1});
		map[0][A][B] = 1;
		map[1][A][B] = 1;
		
		while(!que.isEmpty()) {
			int[] cur = que.poll();
			int a = cur[0];
			int b = cur[1];
			int cnt = cur[2];
			
			if(cnt % 2 == 1) {
				int a_left = a - DA;
				if(a_left < 0) a_left += N;
				int a_right = a + DA;
				if(a_right >= N) a_right -= N;
				
				if(map[0][a_left][b] == 0) {
					map[0][a_left][b] = cnt + 1;
					que.offer(new int[] {a_left, b, cnt+1});
				}
				if(map[0][a_right][b] == 0) {
					map[0][a_right][b] = cnt + 1;
					que.offer(new int[] {a_right, b, cnt+1});
				}
			} else {
				int b_left = b - DB;
				if(b_left < 0) b_left += N;
				int b_right = b + DB;
				if(b_right >= N) b_right -= N;
				
				if(map[1][a][b_left] == 0) {
					map[1][a][b_left] = cnt + 1;
					que.offer(new int[] {a, b_left, cnt+1});
				}
				if(map[1][a][b_right] == 0) {
					map[1][a][b_right] = cnt + 1;
					que.offer(new int[] {a, b_right, cnt+1});
				}
			}
		}
		
		int min = Integer.MAX_VALUE;
		for (int i = 0; i < N; i++) {
			if(map[0][i][i] != 0 && min > map[0][i][i]) min = map[0][i][i];
			if(map[1][i][i] != 0 && min > map[1][i][i]) min = map[1][i][i];
		}
		
		if(min == Integer.MAX_VALUE) System.out.println("Evil Galazy");
		else System.out.println(min - 1);
	}

}
