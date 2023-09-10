#include <bits/stdc++.h>
using namespace std;

int main() {
	int n, m;
	vector<int> name, sum, dp;
    cin >> n >> m;
    name.resize(n+1);
    sum.resize(n+1);
    dp.resize(n+1, -1);
    for (int i = 1; i <= n; i++) {
        cin >> name[i];
        sum[i] = sum[i - 1] + name[i];
    }
    dp[0] = 0;
    dp[1] = (m - name[1]);
    dp[1] *= dp[1];
    int ans = '????';
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
        	//if there it exceeds 
            if (sum[i] - sum[j - 1] + i - j > m)
                continue;
            
            // remained size;
            int r = m - (sum[i] - sum[j - 1] + i - j);
            r *= r;
            r += dp[j-1];
            if (dp[i] == -1 || dp[i] > r)
                dp[i] = r;
        }
    }

    for (int i = 1; i <= n; i++)
        if (sum[n] - sum[i] + n - i <= m)
            ans = min(ans, dp[i]);
    
    cout << ans;
}