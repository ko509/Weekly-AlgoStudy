import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
        
		int T = Integer.parseInt(br.readLine());
		
		for (int t = 0; t < T; t++) {
			int N = Integer.parseInt(br.readLine());
			int[] team = new int[N];
			st = new StringTokenizer(br.readLine());
			int[] v = new int[N];
			
			int count = 0;
			for (int i = 0; i < N; i++) {
				team[i] = Integer.parseInt(st.nextToken()) - 1;
			}
			
			Queue<Integer> que = new LinkedList<>();
			int visit = 2;
			for (int i = 0; i < N; i++) {
				if(v[i] == 0) {
					que.offer(i);
					int start = visit;
					v[i] = visit++;
					while(!que.isEmpty()) {
						int cur = que.poll();
						if(v[team[cur]] != 0) {
							if(v[team[cur]] >= start) {
								count += visit - v[team[cur]];
							}
							break;
						}
						que.offer(team[cur]);
						v[team[cur]] = visit++;;
					}
					
				}
			}
			
			sb.append(N - count).append("\n");
		}
        System.out.print(sb);
	}

}
