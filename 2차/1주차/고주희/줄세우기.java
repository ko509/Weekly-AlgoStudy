import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

// 시간 : 76ms
// 메모리 : 11516KB
public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		int[] children = new int[N];
		int[] cost = new int[N + 1];
		
		for (int i = 0; i < N; i++) {
			children[i] = Integer.parseInt(br.readLine());
		}
		
		int r = 0;
		for (int i = 0; i < N; i++) {
			int max = 0;
			for (int j = 0; j < children[i]; j++) {
				if(max < cost[j]) {
					max = cost[j];
				}
			}
			cost[children[i]] = max + 1;
			if(r < cost[children[i]]) r = cost[children[i]];	
		}
		
		System.out.println(N - r);
	}

}
