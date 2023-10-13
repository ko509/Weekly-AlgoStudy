#include <iostream>
#include <vector>
using namespace std;
#define MAX 1005
int Sum[MAX][MAX];
int solution(vector<vector<int>>board, vector<vector<int>> skill) {
    int answer = 0;
    int sk[6]; // type,r1,c1,r2,c2,degree;
    for (auto i : skill)
    {
        for (int j = 0; j < 6; j++)
            sk[j] = i[j];
        int type = sk[0];
        int r1 = sk[1];
        int c1 = sk[2];
        int r2 = sk[3];
        int c2 = sk[4];
        int degree = sk[5];
        if (type == 1) degree = -degree;
        Sum[r1][c1] += degree;
        Sum[r1][c2 + 1] -= degree;
        Sum[r2 + 1][c1] -= degree;
        Sum[r2 + 1][c2 + 1] += degree;
    }
    int n = board.size();
    int m = board[0].size();
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            Sum[i][j + 1] += Sum[i][j];
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            Sum[j + 1][i] += Sum[j][i];
    for (int i = 0; i < board.size(); i++)
        for (int j = 0; j < board[i].size(); j++)
        {
            if (board[i][j] + Sum[i][j] > 0)
                answer++;
        }
    return answer;
}