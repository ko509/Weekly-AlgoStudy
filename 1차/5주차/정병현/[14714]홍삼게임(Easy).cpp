#include<bits/stdc++.h>
using namespace std;
using piii=tuple<int, int, int>;
int main(){
	int n, a, b, da, db, ans = 0;
	vector<vector<int>> state[2];
	queue<piii> Q;
	cin >> n >> a >> b >> da >> db;
	a%=n; b%=n;
	state[0].resize(n);
	state[1].resize(n);
	for(auto& i : state[0])
		i.resize(n);
	for(auto& i : state[1])
		i.resize(n);
	Q.push({a, b, 1});
	//bfs
	while(Q.size()){	
		auto[a, b, t] = Q.front();
		Q.pop();
		if(a == b){
			ans = t;
			break;
		}	
		if(state[t&1][a][b])
			continue;
		state[t&1][a][b] = t;
		int d = (t&1?da:db);
		Q.emplace(b, (a+d)%n, t+1);
		Q.emplace(b, (n+a-d)%n, t+1);
	}
	if(ans == 0)
		cout << "Evil Galazy";
	else
		cout << ans-1;
}