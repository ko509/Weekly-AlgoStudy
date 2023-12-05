#include <iostream>
#include <vector>

#define MAX_LEN 1001
using namespace std;

int tmp[MAX_LEN];
int step[MAX_LEN];
int lcs[MAX_LEN];

int main(void) {
    ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
    int A;
    cin >> A;

    // 첫번째 값은 미리 넣어놓는다.    
    cin >> tmp[0];
    lcs[0] = tmp[0];
    step[0] = 0;

    int idx = 0;
    for (int i = 1; i < A; ++i) {
        cin >> tmp[i];

        if (lcs[idx] < tmp[i]) {
            // 값이 클 경우에는...
            lcs[++idx] = tmp[i];
            step[i] = idx;
        }
        else {
            // 값이 같거나 작았을 경우
            for (int j = 0; j <= idx; ++j) {
                if (lcs[j] >= tmp[i]) {
                    lcs[j] = tmp[i];
                    step[i] = j;
                    break;
                }
            }

        }
    }
    vector<int> vec;
    for (int i = A - 1; i >= 0; --i) {
        if (idx == step[i]) {
            vec.push_back(tmp[i]);
            --idx;

            if (idx < 0) {
                break;
            }
        }
    }

    int len = (int)vec.size();
    cout << len << '\n';
    for (int i = len - 1; i >= 0; --i) {
        cout << vec[i] << " ";
    }

    return 0;
}
