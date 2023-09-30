// 시간 : 568ms
// 메모리 : 131904KB

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static class SegTree {
		long[] tree;
		int treeSize;
		
		public SegTree(int size) {
			this.treeSize = size * 4;
			this.tree = new long[this.treeSize];
		}
		
		public long init(long[] num, int node, int start, int end) {
			
			if(start == end) {
				return tree[node] = num[start];
			}
			
			return tree[node] = init(num, node * 2, start, (start + end) / 2) + init(num, node * 2 + 1, (start + end) / 2 + 1, end);
		}
		
		public void update(int node, int start, int end, int idx, long diff) {
			
			if(idx < start || end < idx) return;
			
			tree[node] += diff;
			
			if(start != end) {
				update(node * 2, start, (start + end) / 2, idx, diff);
				update(node * 2 + 1, (start + end) / 2 + 1, end, idx, diff);
			}
		}
		
		public long sum(int node, int start, int end, int left, int right) {
			
			if(start > right || end < left) return 0l;
			
			if(left <= start && end <= right) {
				return tree[node];
			}
			
			return sum(node * 2, start, (start + end) / 2, left, right) + sum(node * 2 + 1, (start + end) / 2 + 1, end, left, right);
		}
	}
	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		long[] num = new long[N + 1];
		for (int i = 1; i <= N; i++) {
			num[i] = Long.parseLong(br.readLine());
		}
		
		SegTree tree = new SegTree(N);
		tree.init(num, 1, 1, N);
		
		StringBuilder sb = new StringBuilder();

		for (int i = 0; i < M + K; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			if(a == 1) {
				long c = Long.parseLong(st.nextToken());
				tree.update(1, 1, N, b, c - num[b]);
                num[b] = c;
			} else {
				int c = Integer.parseInt(st.nextToken());
				sb.append(tree.sum(1, 1, N, b, c)).append("\n");
			}
		}
		System.out.println(sb);
	}

}
