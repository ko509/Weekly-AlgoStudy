#include <bits/stdc++.h>
using namespace std;
int main(){
	cin.tie(0)->sync_with_stdio(0);
	vector<pair<int,int>> state;
	int n, q;
	char c;
	cin >> n;
	state.resize(n+1, {-1, 0});
	for(int i = 1, j = 0; i <= n; i++){
		//cout << i << "\n";
		cin >> c;
		if(c == 's'){
			state[i] = {state[j].first, j};
			j = state[j].second;
		}
		else{
			cin >> q;
			if(c == 'a'){
				state[i] = {q, j};
				j = i;
			}
			else{
				state[i] = {state[j].first, j};
				j = state[q].second	;
			}
		}
		cout << state[j].first <<"\n";
	}
}