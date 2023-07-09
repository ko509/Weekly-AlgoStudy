#include <bits/stdc++.h>
using namespace std;

int dx[4] = {1, -1, 0, 0}, dy[4] = {0, 0, 1, -1}, board[30][30] = {0, }, n=0, cnt;
vector <int> v;

int dfs(int x, int y){
	int cnt = 1;
	board[x][y] = 2;
	for(int i = 0; i < 4; i++){
		if(0 <= x+dx[i] && x+dx[i] < n && 0 <= y+dy[i] && y+dy[i] < n && board[x+dx[i]][y+dy[i]] == 1){
			cnt += dfs(x+dx[i], y+dy[i]);
		}
	}
	return cnt;
}

int main(){
	cin >> n;
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++){	
			scanf("%1d", &board[i][j]);
		}
	}
	
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++){
			if(board[i][j] == 1)
				v.push_back(dfs(i, j));
		}
	}
	sort(v.begin(), v.end());
	for(auto i : v)
		cout << i << "\n";
}                   
	}