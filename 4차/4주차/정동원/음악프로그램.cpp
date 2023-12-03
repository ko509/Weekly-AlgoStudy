#include <iostream>
#include <vector>
#include <queue>

#define MAX_LEN 1001
using namespace std;

vector<int> m_vEdge[MAX_LEN];
vector<int> ans;

int visit[MAX_LEN];

int main(void) {
    ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
    int N, M;
    cin >> N >> M;

    for (int i = 0; i < M; ++i) {
        int a;
        cin >> a;

        // 제일 첫번째 값에 대해서는 따로 pre값으로 넣어준다.
        int pre;
        cin >> pre;

        for (int j = 1; j < a; ++j) {
            int b;
            cin >> b;

            m_vEdge[pre].push_back(b);
            ++visit[b];
            pre = b;
        }
    }

    queue<int> que;

    for (int i = 1; i <= N; ++i) {
        if (visit[i] != 0) { continue; }
        que.push(i);
    }

    while (!que.empty()) {
        int node = que.front();
        que.pop();

        ans.push_back(node);

        for (int i = 0; i < (int)m_vEdge[node].size(); ++i) {
            int nexNode = m_vEdge[node][i];
            --visit[nexNode];

            if (visit[nexNode] == 0) {
                que.push(nexNode);
            }
        }
    }

    if (ans.size() != N) {
        cout << 0;
        return 0;
    }

    for (int i = 0; i < (int)ans.size(); ++i) {
        cout << ans[i] << '\n';
    }

    return 0;
}