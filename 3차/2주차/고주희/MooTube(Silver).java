import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// 시간 : 588ms
// 메모리 : 18852KB
public class Main {

	static int[] parent;
	static int[] rank;
	static class Edge implements Comparable<Edge>{
		int p;
		int q;
		int r;
		
		public Edge(int p, int q, int r) {
			this.p = p;
			this.q = q;
			this.r = r;
		}
		
		@Override
		public int compareTo(Edge o) {
			return o.r - this.r;
		}
	}
	
	static class Query implements Comparable<Query> {
		int idx;
		int k;
		int v;
		
		public Query(int idx, int k, int v) {
			this.idx = idx;
			this.k = k;
			this.v = v;
		}
		
		@Override
		public int compareTo(Query o) {
			return o.k - this.k;
		}
	}
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int Q = Integer.parseInt(st.nextToken());
		
		parent = new int[N];
		rank = new int[N];
		
		Edge[] edge = new Edge[N - 1];
		
		for (int i = 0; i < N; i++) {
			parent[i] = i;
			rank[i] = 1;
		}
		
		for (int i = 0; i < N - 1; i++) {
			st = new StringTokenizer(br.readLine());
			int p = Integer.parseInt(st.nextToken()) - 1;
			int q = Integer.parseInt(st.nextToken()) - 1;
			int r = Integer.parseInt(st.nextToken());
			
			edge[i] = new Edge(p, q, r);
		}
		
		Query[] query = new Query[Q];
		for (int i = 0; i < Q; i++) {
			st = new StringTokenizer(br.readLine());
			int k = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken()) - 1;
			
			query[i] = new Query(i, k, v);
		}
		
		Arrays.sort(edge);
		Arrays.sort(query);
		
		int[] res = new int[Q];
		for (Query q : query) {
			int idx = 0;
			while(idx < N - 1 && edge[idx].r >= q.k) {
				union(edge[idx].p , edge[idx].q);
				idx++;
			}
			res[q.idx] = rank[find(q.v)] - 1;
		}
		
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < Q; i++) {
			sb.append(res[i]).append("\n");
		}
		System.out.println(sb);
	}
	
	private static void union(int p, int q) {
		
		int pp = find(p);
		int pq = find(q);
		
		if(pp == pq) return;
        if(rank[pp] >= rank[pq]) {
            parent[pq] = pp;
    		rank[pp] += rank[pq];
        } else {
            parent[pp] = pq;
            rank[pq] += rank[pp];
        }
		
	}

	private static int find(int p) {
		if(parent[p] == p) return p;
		return parent[p] = find(parent[p]);
	}

}
