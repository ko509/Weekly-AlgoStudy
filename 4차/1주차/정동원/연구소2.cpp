// 2044KB, 12ms
// 시도 횟수 : 3회
// 그래프이론, 브루트포스

#include <iostream>
#include <vector>
#include <queue>

#define WALL 1
#define PLACEVIRUS 2

#define MAX_LEN 50
#define MAX_VIRUS_CNT 10
#define MAX_DIR 4
#define MAXVALUE 10000000
using namespace std;

int maps[MAX_LEN][MAX_LEN];
vector<pair<int, int>> vVirus;
bool aVirus[MAX_VIRUS_CNT] = { 0, };

int posX[MAX_DIR] = { -1, 1, 0, 0 };
int posY[MAX_DIR] = { 0, 0, -1, 1 };

int dp[MAX_LEN][MAX_LEN];

void bfs(int _mapLen) {
    queue<pair<int, int>> que;
    for (int i = 0; i < (int)vVirus.size(); ++i) {
        if (aVirus[i] == false) { continue; }
        int x = vVirus[i].first;
        int y = vVirus[i].second;

        dp[y][x] = 0;
        que.push(make_pair(x, y));
    }

    int depth = 0;
    while (!que.empty()) {
        int len = que.size();
        ++depth;

        for (int i = 0; i < len; ++i) {
            pair<int, int> node = que.front();
            que.pop();

            for (int j = 0; j < 4; ++j) {
                int x = node.first + posX[j];
                int y = node.second + posY[j];

                if (x < 0 || y < 0 || x >= _mapLen || y >= _mapLen) { continue; }    // 맵 범위를 벗어나면 패스
                if (maps[y][x] == WALL) { continue; }        // 벽은 통과하지 못한다
                if (dp[y][x] <= depth) { continue; }          // dp가 낮은 곳은 패스

                dp[y][x] = depth;
                que.push(make_pair(x, y));
            }
        }
    }
}

void recursive(int _idx, int _cnt, int _target, int _mapLen, int* _time) {
    // 사용하고자 하는 바이러스의 위치가 확정되었을 때 시도해본다
    if (_cnt == _target) {
        // 모든 dp에 대해서 초기화를 진행
        for (int i = 0; i < _mapLen; ++i) {
            for (int j = 0; j < _mapLen; ++j) {
                dp[i][j] = MAXVALUE;
            }
        }

        bfs(_mapLen);

        int time = 0;
        for (int i = 0; i < _mapLen; ++i) {
            for (int j = 0; j < _mapLen; ++j) {
                if (maps[i][j] == WALL) { continue; }    // 벽이 아닌곳을 제외한 곳에 대한 dp를 확인해서 최댓값을 저장해놓는다
                if (time < dp[i][j]) {
                    time = dp[i][j];
                }
            }
        }

        if (*_time > time) {
            *_time = time;
        }

        return;
    }

    for (int i = _idx; i < (int)vVirus.size(); ++i) {
        aVirus[i] = true;
        recursive(i + 1, _cnt + 1, _target, _mapLen, _time);
        aVirus[i] = false;
    }
    return;
}

int main(void) {
    ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
    int N, M;
    cin >> N >> M;

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> maps[i][j];

            if (maps[i][j] == PLACEVIRUS) {
                vVirus.push_back(make_pair(j, i));
            }
        }
    }

    // 백트래킹을 사용해봅시다
    int time = MAXVALUE;
    recursive(0, 0, M, N, &time);

    time = time == MAXVALUE ? -1 : time;    // 만약 바이러스가 전체로 퍼지지 못하는경우에는 -1을 출력한다
    cout << time;

    return 0;
}