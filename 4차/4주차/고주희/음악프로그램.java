import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

// 시간 : 140ms
// 메모리 : 14852KB
public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int[] before = new int[N + 1];
		List<Integer>[] after = new ArrayList[N + 1];
		boolean[][] prev = new boolean[N + 1][N + 1];
		
		for (int i = 0; i <= N; i++) {
			after[i] = new ArrayList<>();
		}
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int p = 0;
			for (int j = 0; j < n; j++) {
				int singer = Integer.parseInt(st.nextToken());
				prev[p][singer] = true;
				p = singer;
			}
		}
		
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if(prev[i][j]) {
					before[j]++;
					after[i].add(j);
				}
			}
		}
		
		Queue<Integer> que = new LinkedList<>();
		for (int i = 1; i <= N; i++) {
			if(before[i] == 0) {
				que.offer(i);
			}
		}
		
		int cnt = 0;
		StringBuilder sb = new StringBuilder();
		while(!que.isEmpty()) {
			int cur = que.poll();
			sb.append(cur).append("\n");
			cnt++;
			for (int i : after[cur]) {
				before[i]--;
				if(before[i] < 0) {
					System.out.println(0);
					return;
				} else if(before[i] == 0) {
					que.offer(i);
				}
			}
			
		}
		
		if(cnt == N) System.out.println(sb);
		else System.out.println(0);
		
	}

}
