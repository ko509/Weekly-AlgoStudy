#include <iostream>
#include <vector>
using namespace std;
#define MAX 1000005
#define ll long long 
ll n, m, a[MAX], s[MAX], f[1005];
void input()
{
	cin >> n >> m;
	for (ll i = 1; i <= n; i++)
		cin >> a[i];
}
ll solve()
{
	ll res = 0;
	for (ll i = 1; i <= n; i++)
	{
		s[i] = (s[i - 1] + a[i]) % m;
	}

	for (ll i = 0; i <= n; i++)
	{
		f[s[i]]++;
	}
	for (ll i = 0; i < m; i++)
	{
		res += (f[i] * (f[i] - 1)) / 2;
	}
	return res;
}
int main()
{
	cin.tie(0); ios::sync_with_stdio(0);
	input();
	cout << solve();
}
