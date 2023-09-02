#include <bits/stdc++.h>
using namespace std;
int conT[1010] = {0, }, pre[1010] = {0, }, tim[1010] = {0, };
vector <vector <int> > conS;
queue <int> Q;
int main(){
	int t, n, k, a, b, w;
	cin >> t;
	for(int z = 0; z < t; ++z){
		cin >> n >> k;
		conS.resize(n+1);
		for(int i = 1; i <= n; ++i)
			cin >> conT[i];
		
		for(int i = 0; i < k; ++i){
			cin >> a >> b;
			conS[a].push_back(b);
			pre[b]++;
		}
		cin >> w;
		for(int i = 1; i <= n; i++){
			if(!pre[i])
				Q.push(i);
		}
		while(pre[w] > 0){
			a = Q.front();
			Q.pop();
			for(auto i : conS[a]){
				tim[i] = max(tim[i], tim[a]+conT[a]);
                if(--pre[i] == 0)
					Q.push(i);
			}
		}
		while(Q.size())
			Q.pop();
		cout << tim[w] + conT[w] << endl;
		memset(tim, 0, 1010 * sizeof(int));
		memset(conT, 0, 1010 * sizeof(int));
		memset(pre, 0, 1010 * sizeof(int));
		conS.clear();
	}
}
