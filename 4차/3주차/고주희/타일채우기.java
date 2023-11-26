import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 시간 : 80ms
// 메모리 : 11516KB
public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		if(N % 2 == 1) {
			System.out.println(0);
			return;
		}
		
		int[][] dp = new int[N + 1][5];
		
		dp[2][0] = 1;
		dp[2][1] = 1;
		dp[2][2] = 1;
		
		for (int i = 4; i <= N; i += 2) {
			dp[i][0] += dp[i - 2][0] + dp[i - 2][1] + dp[i - 2][2] + dp[i - 2][3] + dp[i - 2][4];
			dp[i][1] += dp[i - 2][0] + dp[i - 2][1] + dp[i - 2][2] + dp[i - 2][3] + dp[i - 2][4];
			dp[i][2] += dp[i - 2][0] + dp[i - 2][1] + dp[i - 2][2] + dp[i - 2][3] + dp[i - 2][4];
			dp[i][3] += dp[i - 2][0] + dp[i - 2][3];
			dp[i][4] += dp[i - 2][1] + dp[i - 2][4];
		}
		
		System.out.println(dp[N][0] + dp[N][1] + dp[N][2] + dp[N][3] + dp[N][4]);
	}

}
