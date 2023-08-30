import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 시간 : 76ms
// 메모리 : 11620KB
public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int X = Integer.parseInt(st.nextToken());
		int Y = Integer.parseInt(st.nextToken());
		
		int D = Integer.parseInt(st.nextToken());
		int T = Integer.parseInt(st.nextToken());
		
		if(D <= T) {
			System.out.println(Math.sqrt(X * X + Y * Y));
		} else {
			double dist = Math.sqrt(X * X + Y * Y);
			
			int N = (int) dist / D;
			
			if(dist - N * D == 0) {
				System.out.println(N * T);
			} else {
				if(N == 0) {
					double two_jump = T + T;
					double only_walk = dist;
					double jump_and_back = T + D - dist;
					
					System.out.println(Math.min(two_jump, Math.min(only_walk, jump_and_back)));
				} else {
					double rest = dist - N * D;
					
					double more_jump = T;
					double only_walk = rest;
					
					System.out.println(Math.min(more_jump, only_walk) + N * T);
				}
			}
		}
	}

}
