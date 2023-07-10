#include <bits/stdc++.h>
using namespace std;
using pii=pair<int, int>;
int dis[4] = {10, 20, 30, 40};
pii backtrack(vector<vector<int>>& users, vector<int>& emoti, vector<int>& buy, int n){
    // for(int i = 0; i < n; i++)
    //     cout << " ";
    // cout << n << "\n";
    if(n == emoti.size()){
        int p = 0, profit = 0;
        for(int i = 0; i < users.size(); i++){
            // cout << i << " : " << buy[i] << "\n";
            if(buy[i] == -1)
                p++;
            else
                profit += buy[i];
        }
        // cout << "\n";
        return {p, profit};
    }
    pii ans = {0, 0};
    vector<int> tbuy = buy;
    for(int t = 0; t < 4; t++){
        for(int i = 0; i < users.size(); i++){
            tbuy[i] = buy[i];
            
            if(tbuy[i] == -1)
                continue;
            
            if(dis[t] >= users[i][0])
                tbuy[i] += emoti[n]*(100-dis[t])/100;
            
            if(tbuy[i] >= users[i][1])
                tbuy[i] = -1;
        }
        ans = max(ans, backtrack(users, emoti, tbuy, n+1));
        tbuy = buy;
    }
    return ans;
}
vector<int> solution(vector<vector<int>> users, vector<int> emoticons) {
    int n = emoticons.size();
    vector<int> ans(2), buy(users.size());
    tie(ans[0], ans[1]) = backtrack(users, emoticons, buy, 0);
    return ans;
}