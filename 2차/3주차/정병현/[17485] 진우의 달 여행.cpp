#include <bits/stdc++.h>
using namespace std;
vector<vector <int>> v[3]; // [0] : from left, [1] : from direct, [2] : from right
vector<vector <int>> board;
int main(){
	int n, m, ans = 2000000000;
	cin >> n >> m;
	for(int i = 0; i < 3; i++){
		v[i].resize(n, vector<int>(m, 2000000000));
	}
	board.resize(n, vector<int>(m));
	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			cin >> board[i][j];
		}
	}
	for(int k = 0; k < 3; k++){
		for(int j = 0; j < m; j++){
			v[k][0][j] = board[0][j];
		}
	}
	for(int i = 1; i < n; i++){
		for(int j = 0; j < m; j++){
			if(j == 0){
				v[1][i][j] = board[i][j] + v[2][i-1][j];
				v[2][i][j] = board[i][j] + min(v[1][i-1][j+1], v[0][i-1][j+1]);
			}
			else if(j == m-1){
				v[1][i][j] = board[i][j] + v[0][i-1][j];
				v[0][i][j] = board[i][j] + min(v[1][i-1][j-1], v[2][i-1][j-1]);
			}
			else{
				v[0][i][j] = board[i][j] + min(v[1][i-1][j-1], v[2][i-1][j-1]);
				v[1][i][j] = board[i][j] + min(v[0][i-1][j], v[2][i-1][j]);
				v[2][i][j] = board[i][j] + min(v[0][i-1][j+1], v[1][i-1][j+1]);
			}
		}
	}
	for(int j = 0; j < m; j++){
		for(int k = 0; k < 3; k++){
			if(v[k][n-1][j] < ans)
				ans = v[k][n-1][j];
		}
	}
	/*
	for(int k = 0; k < 3; k++){
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++)
				cout << v[k][i][j] << " ";
			cout << "\n";
		}
		cout << "\n\n";
	}
	//*/
	cout << ans;
}