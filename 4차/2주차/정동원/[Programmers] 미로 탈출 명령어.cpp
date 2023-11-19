#include <iostream>
#include <vector>
#include <queue>

#define MAX_LEN 51
using namespace std;

string dp[MAX_LEN][MAX_LEN];

int posX[4] = { 0, -1, 1, 0 };
int posY[4] = { 1, 0, 0, -1 };
char words[4] = { 'd', 'l', 'r', 'u' };
vector<char> vec;
string ans;

int getDis(int _x1, int _y1, int _x2, int _y2) {
    int x = _x1 < _x2 ? _x2 - _x1 : _x1 - _x2;
    int y = _y1 < _y2 ? _y2 - _y1 : _y1 - _y2;
    return x + y;
}

bool findFlag = false;

void dfs(int _x, int _y, int _targetX, int _targetY, int _maxX, int _maxY, int _K) {
    if (findFlag) { return; }

    if (_x == _targetX && _y == _targetY && _K == 0) {
        findFlag = true;

        for (int i = 0; i < (int)vec.size(); ++i) {
            ans += vec[i];
        }
        return;
    }

    // 남은 거리 관련 계산
    int dis = getDis(_x, _y, _targetX, _targetY);
    if (_K - dis < 0 || (_K - dis) % 2 != 0) {
        return;
    }

    for (int i = 0; i < 4; ++i) {
        int x = _x + posX[i];
        int y = _y + posY[i];

        if (x < 0 || y < 0 || x >= _maxX || y >= _maxY) { continue; }

        vec.push_back(words[i]);
        dfs(x, y, _targetX, _targetY, _maxX, _maxY, _K - 1);
        vec.pop_back();
    }

    return;
}

string solution(int n, int m, int x, int y, int r, int c, int k) {
    string answer = "";

    dfs(y - 1, x - 1, c - 1, r - 1, m, n, k);
    if (!findFlag)
    {
        return "impossible";
    }

    answer = ans;
    return answer;
}