import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int n, statusFullBit, INF = 987654321;
	static int[][] w;
	static int[][] dp;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		n = Integer.parseInt(br.readLine());
		statusFullBit = (1<<n) -1;
		w = new int[n][n];
		dp = new int[n][statusFullBit];
		for(int i=0; i<n; i++) {
			Arrays.fill(dp[i], -1);
		}
		
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<n; j++) {
				w[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		System.out.println(dfs(0,1)); 
	}
	
	static int dfs(int x, int check) {
        
		if(check == statusFullBit) {
			if(w[x][0] == 0) return INF; 
			else return w[x][0]; 
		}
        
		if(dp[x][check] != -1) return dp[x][check];
        
		dp[x][check] = INF;
        
		for(int i=0; i<n; i++) {
			int next = check | (1<<i); 
            
			if(w[x][i] ==0 || (check & (1<<i)) != 0) continue;
			
			dp[x][check] = Math.min(dp[x][check], dfs(i, next) + w[x][i]);
		}
		
		return dp[x][check];
	}
}
