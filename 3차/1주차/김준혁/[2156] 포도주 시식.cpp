#include <iostream>
using namespace std;
#define MAX 10005
int a[MAX], dp[MAX];
int n;
void input()
{
	cin >> n;
	for (int i = 1; i <= n; i++)
		cin >> a[i];
}
int solve()
{
	int res = 0;
	if (n == 1)
		return a[1];
	if (n == 2)
		return a[1]+a[2];
	dp[1] = a[1];
	dp[2] = a[1] + a[2];
	dp[3] = max(dp[2], max(a[1] + a[3], a[2] + a[3]));
	for (int i = 3; i <= n; i++)
	{
		dp[i] = max(dp[i - 3] + a[i - 1] + a[i], max(dp[i - 2] + a[i], dp[i - 1]));
	}
	return dp[n];
}
int main()
{
	cin.tie(0); ios::sync_with_stdio(0);
	input();
	cout << solve();
}
