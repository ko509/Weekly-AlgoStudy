#include <bits/stdc++.h>
using namespace std;
using pii=pair<int, int>;
int main(){
	int n, s;
	vector<pii> v;
	vector<int> prev, dp;
	cin >> n >> s;
	v.resize(n+1);
	prev.resize(n+1);
	dp.resize(n+1);
	for(int i = 1; i <= n; i++)
		cin >> v[i].first >> v[i].second;
	sort(v.begin()+1, v.end());
	for(int i = 1; i <= n; i++){
		for(prev[i] = prev[i-1]; prev[i] < i; prev[i]++)
			if(v[i].first-v[prev[i]].first < s)
				break;
		prev[i]--;
	}
	for(int i = 1; i <= n; i++){
		dp[i] = dp[prev[i]] + v[i].second;
		dp[i] = max(dp[i], dp[i-1]);
	}
	cout << dp[n];
}