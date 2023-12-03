#include <iostream>
#include <algorithm>
#include <vector>

#define MAX_LEN 16
#define MAXVALUE 2000000000
using namespace std;

int maps[MAX_LEN][MAX_LEN];
int dp[MAX_LEN][1 << MAX_LEN];

int recursive(int _cur, int _visit, int _target, int _len) {
    if (_visit == _target) {
        if (maps[_cur][0] == 0) {
            return MAXVALUE;
        }
        return maps[_cur][0];
    }

    if (dp[_cur][_visit] != -1) {
        return dp[_cur][_visit];
    }
    dp[_cur][_visit] = MAXVALUE;

    for (int i = 0; i < _len; ++i) {
        if (maps[_cur][i] == 0) { continue; }
        if ((_visit & (1 << i)) == (1 << i)) { continue; }

        int a = dp[_cur][_visit];
        int b = maps[_cur][i] + recursive(i, _visit | 1 << i, _target, _len);
        dp[_cur][_visit] = a < b ? a : b;
    }
    return dp[_cur][_visit];
}

int main(void) {
    ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
    int N;
    cin >> N;

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> maps[i][j];
        }
    }

    for (int i = 0; i < MAX_LEN; ++i) {
        for (int j = 0; j < (1 << MAX_LEN); ++j) {
            dp[i][j] = -1;
        }
    }

    cout << recursive(0, 1, (1 << N) - 1, N);

    return 0;
}