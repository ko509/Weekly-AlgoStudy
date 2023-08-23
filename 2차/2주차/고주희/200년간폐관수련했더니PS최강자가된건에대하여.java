import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 시간 : 336ms
// 메모리 : 43728KB
public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		
		int[][] test = new int[N][2];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int p = Integer.parseInt(st.nextToken());
			
			test[i][0] = x;
			test[i][1] = p;
		}
		
		int max = test[0][1];
		int price = max;
		boolean flag = false;
		boolean ice = false;
		
		for (int i = 1; i < N; i++) {
			if(!flag && i == N - 1) break;
			if(test[i][0] >= price) {
				price += test[i][1];
				max = Math.max(max, test[i][1]);
			} else {
				if(flag) {
					ice = true;
					break;
				}
				flag = true;
				if(test[i][1] < max && price - max <= test[i][0]) {					
					price -= max;
					if(test[i][0] < price) {
						ice = true;
						break;
					} else {
						price += test[i][1];
					}
				}
			}
		}
		System.out.println(ice ? "Zzz" : "Kkeo-eok");
		
	}

}
