import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int N, M;
	static int cntPos; // 바이러스를 놓을 수 있는 위치의 개수
	static int cntSpace = 0; // 빈 공간의 개수
	static int minTime = Integer.MAX_VALUE;
	static int[] dr = {-1,1,0,0};
	static int[] dc = {0,0,-1,1};
	
	static int[][] map;
	static ArrayList<int[]> list;
	
	public static void main(String[] args) throws IOException {
		// 입력 초기화
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine(), " ");
		
		N = Integer.parseInt(stk.nextToken()); // 연구소 크기 N
		M = Integer.parseInt(stk.nextToken()); // 놓을 수 있는 바이러스 개수 M
		
		map = new int[N][N];
		list = new ArrayList<int[]>();
		for(int i=0; i<N; i++) { // NxN 연구소
			stk = new StringTokenizer(br.readLine(), " ");
			for(int j=0; j<N; j++) {
				map[i][j] = Integer.parseInt(stk.nextToken());
				if(map[i][j]==2) list.add(new int[] {i,j});  // 바이러스 놓을 수 있는 위치는 리스트로 관리
				if(map[i][j]!=1) cntSpace++; // 빈 칸의 개수 계산
			}
		}
		
		// 바이러스를 놓을 M개의 위치를 고른다
		cntPos = list.size();
		cntSpace = cntSpace - M;
		putVirus(0, 0, new int[M]);
		
		// 결과 출력
		System.out.println(minTime==Integer.MAX_VALUE ? -1 : minTime);
	}
	
	// putVirus(), 바이러스를 놓을 M개의 위치 선정
	public static void putVirus(int cnt, int start, int[] selected) {
		// M개의 위치를 다 골랐으면
		if(cnt==M) {
			// 맵 복사
			int[][] copyMap = copy();
			// 바이러스 확산
			int time = spreadVirus(selected, copyMap);
			// 최소 시간을 달성하면 업데이트
			if(time < minTime) minTime = time;
			return;
		}
		
		// 실행 구문
		for(int i=start; i<cntPos; i++) {
			selected[cnt] = i;
			// i+1번째 위치를 고르러 간다
			putVirus(cnt+1, i+1, selected);
		}
		
		
	}
	
	// spreadVirus(), 바이러스 확산 메서드
	public static int spreadVirus(int[] selected, int[][] copyMap) {
		int time = -1;
		int leftSpace = cntSpace;
		Queue<int[]> q = new ArrayDeque<int[]>();
		boolean[][] visited = new boolean[N][N];
		
		// 초기 바이러스 투입
		for(int idx : selected) {
			int[] pos = list.get(idx); // 선택된 위치에
			copyMap[pos[0]][pos[1]] = -1; // 바이러스 투입
			q.offer(pos); // 바이러스 확산을 위해 큐에 삽입
			visited[pos[0]][pos[1]] = true; // 방문 처리
		}
		
		// BFS
		while(!q.isEmpty()) {
			time++;
			// 백트래킹, 최소 시간보다 크면 더 이상 탐색 X
			if(time > minTime) return Integer.MAX_VALUE;
			
			// Depth 관리
			int len = q.size();
			for(int i=0; i<len; i++) {
				int[] cur = q.poll();
				
				// 바이러스 하나를 꺼내 4방 탐색
				for(int j=0; j<4; j++) {
					int nr = cur[0] + dr[j];
					int nc = cur[1] + dc[j];
					if(nr<0 || nc<0 || nr>=N || nc>=N) continue; // 배열 범위 초과 
					if(visited[nr][nc] || copyMap[nr][nc]==1) continue; // 이미 방문했거나, 벽이거나
					
					// 바이러스 확산
					copyMap[nr][nc] = -1;
					visited[nr][nc] = true;
					q.offer(new int[] {nr,nc});
					// 남은 빈 칸의 개수 감소
					leftSpace--; 
				}
			}
		}
		
		// 만약 바이러스가 존재하지 않는 빈 칸이 남아있으면,
		// 현재 경우는 모든 빈 칸에 바이러스를 퍼뜨릴 수 없으므로 MAX_VALUE 반환
		if(leftSpace > 0) return Integer.MAX_VALUE;
		
		return time;
	}

	// copy(), 배열 복사 메서드
	public static int[][] copy(){
		int[][] copyMap = new int[N][N];
		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++) {
				copyMap[i][j] = map[i][j];
			}
		}
		
		return copyMap;
	}
	
	// print(), 디버깅을 위한 배열 출력 메서드
	public static void print() {
		System.out.println("== 배열 출력 == ");
		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++) {
				System.out.print(map[i][j] + " ");
			}
			System.out.println();
		}
	}
}
