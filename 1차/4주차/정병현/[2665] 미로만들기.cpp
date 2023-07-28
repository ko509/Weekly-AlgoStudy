#include <bits/stdc++.h>
using namespace std;
using pii=pair<int, int>;
int main(){
	int n, board[55][55] = {0, }, visited[55][55] = {0, }, dx[4] = {1, -1, 0, 0}, dy[4] = {0, 0, 1, -1};
	string s;
	cin >> n;
	queue<pii> Q;
	for(int i = 0; i < n; i++){
		cin >> s;
		for(int j = 0; j < n; j++)
			if(s[j] == '1')
				board[i][j] = 1;
	}
	visited[0][0] = 1;
	Q.push({1, 0});
	while(!Q.empty()){
		auto [d, t]= Q.front();
		Q.pop();
		int x = t/50, y = t%50;
		if(visited[x][y] && d > visited[x][y])
			continue;
		//cout << x << " " << y << "\n";
		for(int i = 0; i < 4; i++){
			unsigned int tx = x+dx[i], ty = y+dy[i];
			if(tx >= n || ty >= n)
				continue;
			if(!board[tx][ty]){
				if(visited[tx][ty] && visited[tx][ty] <= d+1)
					continue;
				visited[tx][ty] = d+1;
				Q.emplace(d+1, 50*tx + ty);
			}
			else{
				if(visited[tx][ty] && visited[tx][ty] <= d)
					continue;
				visited[tx][ty] = d;
				Q.emplace(d, 50*tx + ty);
			}
		}
	}
	cout << visited[n-1][n-1]-1;
}