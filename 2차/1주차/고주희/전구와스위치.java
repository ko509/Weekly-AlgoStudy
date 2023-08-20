import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 시간 : 128ms
// 메모리 : 15764KB
public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		boolean[] one = new boolean[N];
		boolean[] two = new boolean[N];
		boolean[] result = new boolean[N];
		
		String light = br.readLine();
		for (int i = 0; i < N; i++) {
			one[i] = light.charAt(i) - '0' == 0 ? true : false;
			two[i] = one[i];
		}
		
		light = br.readLine();
		for (int i = 0; i < N; i++) {
			result[i] = light.charAt(i) - '0' == 0 ? true : false;
		}
		
		// part 1
		int cnt1 = 0;
		
		for (int i = 1; i < N - 1; i++) {
			if(one[i - 1] != result[i - 1]) {
				cnt1++;
				one[i - 1] = !one[i - 1];
				one[i] = !one[i];
				one[i + 1] = !one[i + 1];
			}
		}
		
		if(one[N - 1] != result[N - 1] || one[N - 2] != result[N - 2]) {
			cnt1++;
			one[N - 1] = !one[N - 1];
			one[N - 2] = !one[N - 2];
		}
		
		// part 2
		int cnt2 = 1;
		two[0] = !two[0];
		two[1] = !two[1];
		
		for (int i = 1; i < N - 1; i++) {
			if(two[i - 1] != result[i - 1]) {
				cnt2++;
				two[i - 1] = !two[i - 1];
				two[i] = !two[i];
				two[i + 1] = !two[i + 1];
			}
		}
		
		if(two[N - 1] != result[N - 1] || two[N - 2] != result[N - 2]) {
			cnt2++;
			two[N - 1] = !two[N - 1];
			two[N - 2] = !two[N - 2];
		}
		
		// 
		boolean f1 = true;
		boolean f2 = true;
		for (int i = 0; i < N; i++) {
			if(result[i] != one[i]) f1 = false;
			if(result[i] != two[i]) f2 = false;
		}
		
		if(!f1 && !f2) System.out.println(-1);
		else if(f1 && !f2) System.out.println(cnt1);
		else if(!f1 && f2) System.out.println(cnt2);
		else System.out.println(Math.min(cnt1, cnt2));
	}

}
