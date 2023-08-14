#include <bits/stdc++.h>
using namespace std;
int main(){
	int n, m, dp[1010][1010];
	string s1, s2;
	cin >> s1;
	cin >> s2;
	n = s1.size();
	m = s2.size();
	dp[0][0] = (s1[0] == s2[0]);
	for(int i = 1; i < n; i++)
		if(dp[i-1][0] || s1[i] == s2[0])
			dp[i][0] = 1;
	for(int i = 1; i < m; i++)
		if(dp[0][i-1] || s2[i] == s1[0])
			dp[0][i] = 1;
	for(int i = 1; i < n; i++){
		for(int j = 1; j < m; j++){
			if(s1[i] == s2[j])
				dp[i][j] = dp[i-1][j-1]+1;
			else
				dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
		}
	}
	cout << dp[n-1][m-1];
}