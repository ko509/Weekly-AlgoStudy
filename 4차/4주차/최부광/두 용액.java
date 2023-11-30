import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// [백준2470] 두 용액
public class Main {
	
	static int N;
	static int[] arr;
	
	static int min; // 가장 0에 가까운 값
	static int[] pos; // 가장 0에 가까운 두 용액
	public static void main(String[] args) throws IOException{
		// 값 입력
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		
		arr = new int[N];
		StringTokenizer stk = new StringTokenizer(br.readLine(), " ");
		for(int i=0; i<N; i++) {
			arr[i] = Integer.parseInt(stk.nextToken());
		}
		
		// 배열 오름차순 정렬
		Arrays.sort(arr);
		
		// 슬라이딩 윈도우 탐색
		min = Integer.MAX_VALUE;
		pos = new int[2];
		
		int start = 0;
		int end = N-1;
		while(start<end) {
			// 혼합 용액의 특성값을 계산한다
			int sum = arr[start] + arr[end];
			// 최소값인지 확인 후 업데이트한다
			if(Math.abs(sum) < min) {
				min = Math.abs(sum);
				pos[0] = start;
				pos[1] = end;
			}
			// 특성값에 따라 다음 포인터 조정
			if(sum > 0) { // 오른쪽 포인터를 왼쪽으로 한 칸 옮긴다
				end--;
			}else if(sum < 0) { // 왼쪽 포인터를 오른쪽으로 한 칸 옮긴다
				start++;
			}else { // 0이라면 이미 최소값이므로 break
				break;
			}
		}
		
		// 결과 출력
		System.out.println(String.format("%d %d", arr[pos[0]], arr[pos[1]]));
	}
}
