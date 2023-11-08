import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

// 시간 : 76ms
// 메모리 : 11528KB
public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		long X = Long.parseLong(st.nextToken());
		long Y = Long.parseLong(st.nextToken());
		long W = Long.parseLong(st.nextToken());
		long S = Long.parseLong(st.nextToken());
		
		long max = X;
		long min = Y;
		
		if(X < Y) {
			max = Y;
			min = X;
		}
		
		long total = 0l;
		
		if(S <= W) {
			total += min * S;
			if((max - min) % 2 == 0) {
				total += (max - min) * S;
			} else {
				total += (max - min - 1) * S + W;
			}
		} else if(S <= W * 2) {
			total += min * S + (max - min) * W;
		} else {
			total += (max + min) * W;
		}
		
		System.out.println(total);
	}

}
