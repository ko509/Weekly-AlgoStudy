import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

// [백준2623번] 음악프로그램
public class Main {
	static int N; // 가수의 수
	static int M; // 보조 PD의 수
	static int left; // 남은 가수의 수
	static int[][] graph; // 진입 차수 그래프
	static int[] inDegree; // 진입 차수 배열
	static boolean[] visited; // 방문 여부 체크 배열
	public static void main(String[] args) throws IOException {
		// 값 입력
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(stk.nextToken());
		M = Integer.parseInt(stk.nextToken());
		
		left = N;
		graph = new int[N+1][N+1];
		inDegree = new int[N+1];
		visited = new boolean[N+1];

		// 각 보조 PD에 대해 가수들의 순서를 진입 차수 그래프에 기록한다
		for(int i=0; i<M; i++) {
			stk = new StringTokenizer(br.readLine(), " ");
			int n = Integer.parseInt(stk.nextToken()); // 해당 보조 PD가 담당하는 가수의 수
			int before = Integer.parseInt(stk.nextToken()); // 가장 첫 번째로 나와야 하는 가수
			for(int j=1; j<n; j++) {
				int after = Integer.parseInt(stk.nextToken()); // 다음으로 나와야 하는 가수
				if(graph[after][before]==0) { // 처음 입력되었을 때만
					graph[after][before]=1; // after의 진입차수 증가
					inDegree[after]++;					
				}
				
				// before보다 먼저 나와야 하는 가수가 더 있는지 확인
				// before보다 먼저 나와야 하는 가수는 after보다도 먼저 나와야 한다
				if(inDegree[before] > 0) {
					for(int k=1; k<n; k++) {
						// 이미 after 그래프에 기록된 가수라면 패스하고
						// 그렇지 않다면 after의 진입차수 그래프에 기록한다
						if(graph[before][k]!=0 && graph[after][k]==0) {
							graph[after][k]=1;
							inDegree[after]++;
						}
					}
				}
				
				before = after; 
			}
		}
		
		// 진입 차수가 0인 정점 찾기 반복
		visited = new boolean[N+1];
		Queue<Integer> queue = new ArrayDeque<Integer>();
		StringBuilder sb = new StringBuilder(); // 결과를 저장할 StringBuilder
		
			// 이미 진입 차수가 0인 정점을 먼저 넣어놓고 시작한다
			for(int i=1; i<=N; i++) {
				if(inDegree[i]==0) {
					queue.offer(i);
					visited[i] = true;
				}
			}
		
			// 큐가 빌 때까지 반복
			while(!queue.isEmpty()) {
				// 큐에서 가수 한 명을 꺼낸다
				int cur = queue.poll();
				left--;
				sb.append(String.format("%d\n", cur));
				// 해당 가수와 관련된 정점들의 진입 차수를 1씩 감소시킨다
				for(int i=1; i<=N; i++) {
					if(graph[i][cur]>0) {
						graph[i][cur]=0;
						inDegree[i]--;
						// 진입차수가 0이 되었는지 확인하고, 0이라면 큐에 넣는다
						if(inDegree[i]==0) {
							visited[i] = true;
							queue.offer(i);
						}
					}
				}
				
			}
		
		// 결과 출력
		if(left==0) System.out.print(sb);
		else System.out.print(0);
	}
}
