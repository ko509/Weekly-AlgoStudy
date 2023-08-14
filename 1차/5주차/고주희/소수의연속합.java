import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

// 시간 : 204ms
// 메모리 : 16684KB
public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		boolean[] num = new boolean[4000001];
		
		for (int i = 2; i <= 2000; i++) {
			if(num[i]) continue;
			int tmp = 2;
			while(tmp * i < 4000001) {
				num[tmp * i] = true;
				tmp++;
			}
		}
		
		int start = 2;
		int end = 2;
		int sum = 2;
		int cnt = 0;
		
		while(start <= end && end < 4000001) {
			
			if(sum < N) {
				end++;
				while(num[end]) {
                    end++;
					if(end > 4000000) break;
				}
				sum += end;
			} else if(sum > N) {
				sum -= start;
				start++;
				while(num[start]) {
                    start++;
                    if(start > end) break;
                }
			} else {
				cnt++;
				end++;
				while(num[end]) {
                    end++;
					if(end > 4000000) break;
				}
				sum += end;
			}
		}
		
		System.out.println(cnt);
	}

}
