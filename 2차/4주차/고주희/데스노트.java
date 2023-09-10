import java.awt.Checkbox;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

	static int N;
	static int M;
	static int[] name;
	static int[][] dp;
	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		name = new int[N];
		dp = new int[1000][1002];
		for (int i = 0; i < N; i++) {
			name[i] = Integer.parseInt(br.readLine());
		}
		
		int idx = 1;
		int cnt = name[0] + 1;
		
		for (int i = 0; i < 1000; i++) {
			Arrays.fill(dp[i], -1);
		}
		
		System.out.println(deathnote(idx, cnt));
	}
	
	private static int deathnote(int idx, int cnt) {
		
		if(idx == N) return 0;
		int tmp = dp[idx][cnt];
		if(tmp != -1) return tmp;
		
		int left = M - cnt + 1;
		tmp = deathnote(idx + 1, name[idx] + 1) + (left * left);
		
		if(cnt + name[idx] <= M) {
			tmp = Math.min(deathnote(idx + 1, cnt + name[idx] + 1), tmp);
		}
		
		dp[idx][cnt] = tmp;
		return tmp;
	}
	

}
