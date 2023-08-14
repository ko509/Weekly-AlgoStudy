import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		
		StringBuilder sb = new StringBuilder();
		for(int t = 0; t < T; t++) {
			int N = Integer.parseInt(br.readLine());
			PriorityQueue<Long> que = new PriorityQueue<>(new Comparator<Long>() {

				@Override
				public int compare(Long o1, Long o2) {
					return Long.compare(o1, o2);
				}
			});
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				que.offer(Long.parseLong(st.nextToken()));
			}
			
			long answer = 0;
			while(que.size() > 1) {
				long a = que.poll();
				long b = que.poll();
				answer += a + b;
				que.offer(a + b);
			}
			
			sb.append(answer).append("\n");
		}
		System.out.println(sb);
	}

}
