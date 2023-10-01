#include <iostream>
using namespace std;
#define MAX 4099999
#define ll long long
ll n, m, k, a, b, c;
ll arr[MAX];
ll SIZE = 2;
void input()
{
	cin >> n >> m >> k;
	while (SIZE < n)
		SIZE <<= 1;
		SIZE <<= 1;
	for (ll i = SIZE/2; i < SIZE/2+n; i++)
		cin >> arr[i]; // 리프부터 채우기
}
void construct()
{
	for (ll i = SIZE / 2 - 1; i > 0; --i) // 리프의 윗 레벨 노드부터 세그먼트 트리 생성
		arr[i] = arr[i * 2] + arr[i * 2 + 1];
}
ll sum(ll L, ll R, ll num, ll curL, ll curR)
{
	if (R < curL || curR < L) return 0;
	if (L <= curL && curR <= R) return arr[num];
	ll mid = (curL + curR) / 2;
	return sum(L, R, num * 2, curL, mid) + sum(L, R, num * 2 + 1, mid + 1, curR);
}
void update(ll idx, ll val)
{
	idx += SIZE / 2 - 1;
	arr[idx] = val;
	while (idx > 1)
	{
		idx /= 2;
		arr[idx] = arr[idx * 2] + arr[idx * 2 + 1];
	}
	return;
}
int main()
{
	cin.tie(0); ios::sync_with_stdio(0);
	input();
	construct();

	for (ll i = 0; i < m + k; i++)
	{
		cin >> a >> b >> c;
		if (a == 1)
			update(b, c);
		else
			cout << sum(b-1, c-1, 1, 0, SIZE/2-1) << "\n";
	}
}
