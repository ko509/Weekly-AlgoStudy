import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		
		int[] past = new int[N+1];
		int[] answer = new int[N+1];
		int cur = 0;
		answer[0] = -1;
		StringBuilder sb = new StringBuilder();
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			char op = st.nextToken().charAt(0);
			
			if(op == 'a') {
				int n = Integer.parseInt(st.nextToken());
				answer[i] = n;
				past[i] = cur;
				cur = i;
			} else if(op == 's') {
				answer[i] = answer[cur];
				past[i] = cur;
				cur = past[cur];
			} else {
				int n = Integer.parseInt(st.nextToken());
				answer[i] = answer[cur];
				past[i] = cur;
				cur = past[n];
			}
			sb.append(answer[cur]).append("\n");
		}
		System.out.print(sb);
	}

}
