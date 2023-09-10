#include <bits/stdc++.h>
using namespace std;
using uint=unsigned int;
using pii=pair<int, int>;
vector<int> visited;
vector<pii> person;
vector<vector<int>> board, dist;

void FW(int n){
	n*=n;
	for(int k = 0; k < n; k++){
		for(int i = 0; i < n; i++)
			for(int j = 0; j < n; j++)
				dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
	}
}

int main(){
	cin.tie(0)->sync_with_stdio(0);	
	int n, m, f, a, b, c, d, p, dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
	cin >> n >> m >> f;
	board.resize(n);
	for(auto& i : board)
		i.resize(n);
	dist.resize(n*n);
	for(auto& i : dist)
		i.resize(n*n, '????');
	visited.resize(m);
	person.resize(m);
	for(auto& i : board)
		for(auto& j : i)
			cin >> j;
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++){
			if(board[i][j])
				continue;
			int pp = n*i + j;
			dist[pp][pp] = 0;
			for(int k = 0; k < 4; k++){
				uint tx = i+dx[k], ty = j+dy[k];
				if(tx >= n || ty >= n)
					continue;
				if(board[tx][ty])
					continue;
				int tp = n*tx + ty;
				dist[pp][tp] = 1;
				dist[tp][pp] = 1;
			}
		}
	}
	FW(n);
	cin >> a >> b;
	p = n*(a-1) + b-1;
	for(int i = 0; i < m; i++){
		cin >> a >> b >> c >> d;
		person[i] = {n*(a-1)+b-1, n*(c-1)+d-1};
	}
	sort(person.begin(), person.end());
//	for(auto& i : dist){
//		for(auto& j : i)
//			cout << j << " ";
//		cout << "\n";
//	}
//	cout << "\n";
	int t = m;
	while(t--){
		int d = n*n;
		int dst = 0;
		//cout << p << "\n";
		for(int i = 0; i < m; i++){
			if(visited[i])
				continue;
			if(dist[p][person[i].first] < d){
				d = dist[p][person[i].first];
				dst = i;
			}
			//cout << "  " << i << " " << dist[p][person[i].first] << "\n";
		}
		if(d == n*n){
			f = -1;
			break;
		}
		int dd = dist[person[dst].first][person[dst].second];
//		cout << "\n";
//		cout << dst << "\n";
//		cout << f << " " << d << " " << dist[person[dst].first][person[dst].second] << "\n";
//		cout << "\n\n";
		f -= d + dd;
		if(f < 0){
			f = -1;
			break;
		}
		p = person[dst].second;
		f += 2*dd;
		visited[dst] = 1;
	}
	//cout << "\n";
	cout << f;
}