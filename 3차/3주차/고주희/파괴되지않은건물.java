class Solution {
    public int solution(int[][] board, int[][] skill) {
        int N = board.length;
        int M = board[0].length;
        int[][] tmp = new int[N][M];
        for (int[] s : skill) {
            int type = s[0];
            int r1 = s[1];
            int c1 = s[2];
            int r2 = s[3];
            int c2 = s[4];
            int degree = s[5];
            
            if(type == 1) degree *= -1;
            
            tmp[r1][c1] += degree;
            if(c2 < M - 1) tmp[r1][c2 + 1] -= degree;
            if(r2 < N - 1) tmp[r2 + 1][c1] -= degree;
            if(c2 < M - 1 && r2 < N - 1) tmp[r2 + 1][c2 + 1] += degree;
        }
        int answer = 0;
        for (int i = 1; i < N; i++) {
            for (int j  = 0; j < M; j++) {
                tmp[i][j] += tmp[i - 1][j];
            }
        }
        for(int j = 1; j < M; j++) {
            for(int i = 0; i < N; i++) {
                tmp[i][j] += tmp[i][j - 1];
            }
        }
        
        for(int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if(tmp[i][j] + board[i][j] > 0) answer++;
            }
        }
        return answer;
    }
}
