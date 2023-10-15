#include <iostream>
#include <queue>
using namespace std;
#define MAX 200002
int board[MAX];
int n, k;
queue <int> q;
void input()
{
	fill(board, board + MAX, -1);
	cin >> n >> k;
}
int solve()
{
	board[n] = 0;
	q.push(n);
	while (!q.empty())
	{
		int cur = q.front(); q.pop();
		if (cur == k)
			return board[k];
		int t = cur;
		while (t != 0 && (t < MAX))
		{
			t *= 2;
			if (t >= MAX) break;
			if (board[t] == -1) q.push(t); // 0초 순간이동
			board[t] = board[cur];
		}

		if (cur > 0 && board[cur - 1] == -1)
		{
			q.push(cur - 1);
			board[cur - 1] = board[cur] + 1;
			t = cur - 1;
			while (t != 0 && (t < MAX))
			{
				t *= 2;
				if (t >= MAX) break;
				if (board[t] == -1) q.push(t); // 0초 순간이동
				board[t] = board[cur];
			}
		} // -1칸 이동
		if (cur < MAX && board[cur + 1] == -1)
		{
			q.push(cur + 1);
			board[cur + 1] = board[cur] + 1;
			t = cur + 1;
			while (t != 0 && (t < MAX))
			{
				t *= 2;
				if (t >= MAX) break;
				if (board[t] == -1) q.push(t); // 0초 순간이동
				board[t] = board[cur];
			}
		} // +1칸 이동

	}
	return board[k];
}
int main()
{
	cin.tie(0); ios::sync_with_stdio(0);
	input(); cout << solve();
}
