import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		int[][] wine = new int[N+1][3];
		
		for (int i = 1; i <= N; i++) {
			int n = Integer.parseInt(br.readLine());
			wine[i][0] = Math.max(Math.max(wine[i - 1][1], wine[i - 1][2]), wine[i - 1][0]);
			wine[i][1] = wine[i - 1][0] + n;
			wine[i][2] = wine[i - 1][1] + n;
		}
		
		System.out.println(Math.max(wine[N][0], Math.max(wine[N][1], wine[N][2])));
	}

}
