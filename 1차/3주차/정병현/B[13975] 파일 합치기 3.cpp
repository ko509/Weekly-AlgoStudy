#include <bits/stdc++.h>
using namespace std;
using ll=long long;
int main(){
	cin.tie(0)->sync_with_stdio(0); // fastio
	ll T, n, t, ans;
	priority_queue<ll, vector<ll>, greater<ll>> pq; //file size priority_queue for two smallest files
	cin >> T;
	while(T--){
		ans = 0;
		cin >> n;
		for(int i = 0; i < n; i++){ // input
			cin >> t;
			pq.push(t);
		}
		while(pq.size() > 1){ // while last one file is remaining
			ll a = pq.top();
			pq.pop();
			ll b = pq.top();
			pq.pop();
			ans += a+b; // merge two smallest file
			pq.push(a+b);
		}
		pq.pop();
		cout << ans << "\n";
	}
}