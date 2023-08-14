#include <bits/stdc++.h>
using namespace std;
using pii=pair<int, int>;
int main(){
	int n, M;
	vector<int> m, c;
	vector<int> dp;
	cin >> n >> M;
	m.resize(n);
	c.resize(n);
	dp.resize(10001);
	for(int& i : m)
		cin >> i;
	for(int& i : c)
		cin >> i;
	// knapsack
	for(int i = 0; i < n; i++){
		int mm = m[i];
		int cc = c[i];
		for(int i = 10000; i >= cc; i--){
			dp[i] = max(dp[i], dp[i-cc] + mm);
		}
	}
	int ans = 10000; 	
	for(int i = 10000; i >= 0; i--){
		if(dp[i] >= M)
			ans = i;
	}
	cout << ans;
}