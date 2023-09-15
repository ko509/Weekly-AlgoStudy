#include <bits/stdc++.h>
using namespace std;
using uint=unsigned int;
using pii=pair<int, int>;
int n, m, dx[] = {1, 0, -1, 0}, dy[] = {0, 1, 0, -1};
vector<vector<int>> board, checking;
vector<pii> cctv;
int check(){
	int ret = 0;
	for(auto cv : checking){
		for(int i : cv){
			int tx = i/m, ty = i%m;
			if(board[tx][ty] == 0)
				board[tx][ty] = 7;
		}
	}
	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			ret += !board[i][j];
			//cout << board[i][j] << " ";
		}
		//cout << '\n';
	}
		
			
		
	for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++)
			if(board[i][j] == 7)
				board[i][j] = 0;
	//cout << "\n\n";
	return ret;
}

int dfs(int p){
	if(p == cctv.size())
		return check();
	auto[t, pos] = cctv[p];
	int x = pos/m, y = pos%m;
	int ans = 1000000;	
	if(t == 5){
		for(int k = 0; k < 4; k++){
			uint tx = x, ty = y;
			while(1){
				tx += dx[k];
				ty += dy[k];
				if(tx >= n || ty >= m || board[tx][ty] == 6)
					break;
				checking[p].push_back(m*tx + ty);
			}
		}
		ans = min(ans, dfs(p+1));
		checking[p].clear();
	}
	if(t == 2){
		for(int i = 0; i < 2; i++){
			for(int k = 0; k < 4; k++){
				if((k+i)&1)
					continue;
				uint tx = x, ty = y;
				while(1){
					tx += dx[k];
					ty += dy[k];
					if(tx >= n || ty >= m || board[tx][ty] == 6)
						break;
					checking[p].push_back(m*tx + ty);
				}
			}
			ans = min(ans, dfs(p+1));
			checking[p].clear();
		}
	}
	else{
		for(int i = 0; i < 4; i++){
			for(int k = 0; k < 4; k++){
				if(t == 1 && k != i)
					continue;
				else if(t == 3 && (k == i || k== (i+1)%4))
					continue;	
				else if(t == 4 && k == i)
					continue;
				uint tx = x, ty = y;
				while(1){
					tx += dx[k];
					ty += dy[k];
					if(tx >= n || ty >= m || board[tx][ty] == 6)
						break;
					checking[p].push_back(m*tx + ty);
				}
			}
			ans = min(ans, dfs(p+1));
			checking[p].clear();
		}
	}
	return ans;
}

int main(){
	cin >> n >> m;
	board.resize(n);
	for(int i = 0; i < n; i++){
		board[i].resize(m);
		for(int j = 0; j < m; j++){
			cin >> board[i][j];
			if(board[i][j] != 0 && board[i][j] != 6)
				cctv.emplace_back(board[i][j], m*i + j);
		}
	}
	checking.resize(cctv.size());
	cout << dfs(0);
}