import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int N;
	static int minDiff = Integer.MAX_VALUE;
	static int[] liquid;
	static int[] minPair = new int[2];
	
	public static void main(String[] args) throws Exception {
		// 입력 초기화
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine()); // 용액의 수
		
		StringTokenizer stk = new StringTokenizer(br.readLine(), " ");
		liquid = new int[N]; // N개의 용액
		for(int i=0; i<N; i++) {
			liquid[i] = Integer.parseInt(stk.nextToken());
		}
		
		// 모든 용액에 대해 이분 탐색
		for(int i=0; i<N; i++) {
			// 초기 값
			// 현재 값과 혼합하여 0과 가장 가까워 지려면 liquid * (-1) 필요
			int start = i+1;
			int end = N-1;
			int target = liquid[i] * (-1);
			
			// target과 가까운 값을 찾는다
			while(start <= end) {
				// 중앙값 
				int mid = (start + end) / 2;
				int sum = Math.abs(liquid[mid] + liquid[i]);
				if(sum < minDiff) {
					minDiff = sum;
					minPair[0] = i;
					minPair[1] = mid;
				}
				// 다음 값 탐색
				// target보다 크면 왼쪽 탐색, target보다 작으면 오른쪽 탐색
				if(liquid[mid] >= target) end = mid-1;
				else start = mid+1;
			}
		}
		
		// 결과 출력 : 특성값이 0에 가장 가까운 용액
		System.out.println(liquid[minPair[0]] + " " + liquid[minPair[1]]);
	}
}
