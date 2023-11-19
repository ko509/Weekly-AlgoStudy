#include <string>
#include <vector>

#define MAX_LEN 300
using namespace std;

int dp[MAX_LEN][MAX_LEN];

int solution(int alp, int cop, vector<vector<int>> problems) {
    int answer = 0;
    int top_alp = 0, top_cop = 0;

    for (int i = 0; i < MAX_LEN; ++i) {
        for (int j = 0; j < MAX_LEN; ++j) {
            dp[i][j] = 100000000;
        }
    }

    for (int i = 0; i < (int)problems.size(); ++i) {
        if (top_alp < problems[i][0]) {
            top_alp = problems[i][0];
        }

        if (top_cop < problems[i][1]) {
            top_cop = problems[i][1];
        }
    }

    alp = alp < top_alp ? alp : top_alp;
    cop = cop < top_cop ? cop : top_cop;

    dp[alp][cop] = 0;
    int indexX = 0, indexY = 0;
    for (int i = alp; i <= top_alp; ++i) {
        for (int j = cop; j <= top_cop; ++j) {
            indexX = min(i + 1, top_alp);
            indexY = min(j + 1, top_cop);

            dp[indexX][j] = min(dp[indexX][j], dp[i][j] + 1);
            dp[i][indexY] = min(dp[i][indexY], dp[i][j] + 1);

            for (int z = 0; z < (int)problems.size(); ++z) {
                int alp_ans = problems[z][0];
                int cop_ans = problems[z][1];
                int alp_plus = problems[z][2];
                int cop_plus = problems[z][3];
                int cost = problems[z][4];

                if (i < alp_ans || j < cop_ans) { continue; }
                indexX = min(i + alp_plus, top_alp);
                indexY = min(j + cop_plus, top_cop);
                dp[indexX][indexY] = min(dp[indexX][indexY], dp[i][j] + cost);
            }
        }
    }

    return answer = dp[top_alp][top_cop];
}