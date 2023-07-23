import java.util.*;

class Solution {
    public int solution(int[][] matrix_sizes) {
     
        int N = matrix_sizes.length;
        
        int[][] dp = new int[N][N];
        
        for(int i = 1; i < N; i++) {
            int b = -1;
            for (int a = 0; a < N; a++) {
                b = i + a;
                
                if(b >= N) break;
                dp[a][b] = 987654321;
                for(int p = a; p < b; p++) {
                    dp[a][b] = Math.min(dp[a][b], dp[a][p] + dp[p + 1][b] + matrix_sizes[a][0] * matrix_sizes[p + 1][0] * matrix_sizes[b][1]);
                }
            }
        }
        
        return dp[0][N-1];
    }
}
