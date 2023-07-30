import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 시간 : 116ms
// 메모리 : 16544KB
public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str1 = br.readLine();
		String str2 = br.readLine();
		
		int N = str1.length();
		int M = str2.length();
		
		int[][] map = new int[N+1][M+1];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if(str1.charAt(i) == str2.charAt(j)) {
					map[i+1][j+1] = map[i][j] + 1;
				} else {
					map[i+1][j+1] = Math.max(map[i][j+1], map[i + 1][j]);
				}
			}
		}
		
		System.out.println(map[N][M]);
	}

}
