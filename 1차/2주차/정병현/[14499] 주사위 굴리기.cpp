#include <bits/stdc++.h>
using namespace std;
using uint=unsigned int;
void rn(vector<int>& v);
void rs(vector<int>& v);
void rw(vector<int>& v);
void re(vector<int>& v);
int main(){
	cin.tie(0)->sync_with_stdio(0);
	int n, m, x, y, q, t, dy[5] = {0, 1, -1, 0, 0}, dx[5] = {0, 0, 0, -1, 1};
	vector<vector<int>> board;
	vector<int> dice(6);
	void (*rotate[5])(vector<int>& v) = {0, re, rw, rn, rs};
	cin >> n >> m >> x >> y >> q;
	board.resize(n);
	for(auto&i : board)
		i.resize(m);
	for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++)
			cin >> board[i][j];
			
	for(int i = 0; i < q; i++){
		cin >> t;
		uint tx = x + dx[t], ty = y+dy[t];
		//cout << tx << " " << ty << "\n";
		if(tx >= n || ty >= m)
			continue;
		rotate[t](dice);
		if(board[tx][ty] == 0)
			board[tx][ty] = dice[0];
		else{
			dice[0] = board[tx][ty];
			board[tx][ty] = 0;
		}
		x = tx; y = ty;
		cout << dice[2];
//		for(auto i : dice)
//			cout << i << " ";
		cout << "\n";
	}
}

void rn(vector<int>& v){
	int t = v[0];
	v[0] = v[1];
	v[1] = v[2];
	v[2] = v[3];
	v[3] = t;
}

void rs(vector<int>& v){
	int t = v[0];
	v[0] = v[3];
	v[3] = v[2];
	v[2] = v[1];
	v[1] = t;
}

void rw(vector<int>& v){
	int t = v[0];
	v[0] = v[4];
	v[4] = v[2];
	v[2] = v[5];
	v[5] = t;
}

void re(vector<int>& v){
	int t = v[0];
	v[0] = v[5];
	v[5] = v[2];
	v[2] = v[4];
	v[4] = t;
}
