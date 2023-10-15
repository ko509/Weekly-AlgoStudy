#include <iostream>
#include <stack>
#include <queue>
using namespace std;
#define MAX 100002
int board[MAX]; // 1บฮลอ
int t, n;
stack <int> s;
bool vis[MAX];
queue <int> q;
void input()
{
	fill(board, board + MAX, 0);
	fill(vis, vis + MAX, false);
	cin >> n;
	for (int i = 1; i <= n; i++)
		cin >> board[i];

}
int solve()
{
	for (int i = 1; i <= n; i++)
	{
		s.push(i);
		while (!s.empty())
		{
			int cur = s.top();
			s.pop();
			if (board[i] == -1) continue;

			if (vis[cur] == false)
			{
				vis[cur] = true;
				q.push(board[cur]);
				s.push(board[cur]);
			}
			else
			{
				while (!q.empty())
				{
					if (q.front() == board[cur])
					{
						while (!q.empty())
						{
							board[q.front()] = -1;
							q.pop();
						}
						while (!s.empty())
						{
							s.pop();
						}
					}
					else
						q.pop();
				}
			}
		}
	}
	int cnt = 0;
	for (int i = 1; i <= n; i++)
	{
		if (board[i] != -1) cnt++;
	}
	return cnt;
}
int main()
{
	cin.tie(0); ios::sync_with_stdio(0);
	cin >> t;
	while (t--)
	{
		input();
		cout << solve() << "\n";
	}
}