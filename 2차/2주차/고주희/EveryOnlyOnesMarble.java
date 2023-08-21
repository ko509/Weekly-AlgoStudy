import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// 시간 : 96ms
// 메모리 : 13056KB
public class Main {

	static int N;
	static long S;
	static int W;
	static int START;
	static int ILAND;
	static int LAND;
	static int SOCIAL;
	static int S_MONEY;
	static int UNIVERSE;
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		N = 4 * n - 4;
		S = Long.parseLong(st.nextToken());
		W = Integer.parseInt(st.nextToken());
		int G = Integer.parseInt(st.nextToken());
		
		Queue<int[]> goldkey = new LinkedList<>();
		
		for (int i = 0; i < G; i++) {
			st = new StringTokenizer(br.readLine());
			int op = Integer.parseInt(st.nextToken());
			int x = Integer.parseInt(st.nextToken());
			goldkey.offer(new int[] {op, x});
		}
		
		int[] map = new int[N];
		
		START = 0;
		ILAND = n - 1;
		SOCIAL = 2 * n - 2;
		UNIVERSE = 3 * n - 3;
		LAND = 0;
		
		for (int i = 0; i < N; i++) {
			if(i == START || i == ILAND || i == SOCIAL || i == UNIVERSE) {
				map[i] = -2;
				continue;
			}
			st = new StringTokenizer(br.readLine());
			char loc = st.nextToken().charAt(0);
			if(loc == 'G') {
				map[i] = -1;
			} else {
				int cost = Integer.parseInt(st.nextToken());
				map[i] = cost;
				LAND++;
			}
		}
		int I = Integer.parseInt(br.readLine());
		
		int l = 0;
		int iland = 0;
		S_MONEY = 0;
		
		for (int t = 0; t < I; t++) {
			st = new StringTokenizer(br.readLine());
			int d1 = Integer.parseInt(st.nextToken());
			int d2 = Integer.parseInt(st.nextToken());
			
			if(l == ILAND) {
				if(d1 == d2) {
					iland = 3;
					continue;
				} else if(iland == 3) {
					iland = 0;
				} else {
					iland++;
					continue;
				}
			} 
			
			int next = l + d1 + d2;
			
			if(next >= N) {
				S += W * next / N;
				next %= N;
			}
			
			l = after_move(next, l, map, goldkey);
		}
		
		if(LAND == 0) System.out.println("WIN");
		else {
			System.out.println("LOSE");
		}
	}

	
	static int after_move(int next, int l, int[] map, Queue<int[]> goldkey) {
		
		if(next == START) {
			return START;
		}
		
		if(next == SOCIAL) {
			S += S_MONEY;
			S_MONEY = 0;
			return next;
		}
		
		if(next == UNIVERSE) {
			S += W;
			return START;
		}
		
		if(map[next] > 0) {
			if(S >= map[next]) {
				S -= map[next];
				map[next] = 0;
				LAND--;
			}
		} else if(map[next] == -1) {
			int[] cur = goldkey.poll();
			goldkey.offer(cur);
			int op = cur[0];
			if(op == 1) {
				S += cur[1];
			} else if(op == 2) {
				S -= cur[1];
				if(S < 0) {
					System.out.println("LOSE");
					System.exit(0);
				}
			} else if(op == 3) {
				S -= cur[1];
				S_MONEY += cur[1];
				if(S < 0) {
					System.out.println("LOSE");
					System.exit(0);
				}
			} else {
				l = next;
				next += cur[1];
				if(next >= N) {
					S += W * next / N;
					next %= N;
				}
				return after_move(next, l, map, goldkey);
			}
		}
		
		return next;
	}
}
