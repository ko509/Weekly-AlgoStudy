#include <iostream>

#define MAX_LEN 1000
using namespace std;

int arr[MAX_LEN];
int fDp[MAX_LEN];   // 앞에서 부터 확인하는 DP
int bDp[MAX_LEN];   // 뒤에서 부터 확인하는 DP
int temp[MAX_LEN];

void reset_arr(int _n) {
    for (int i = 0; i < _n; ++i) {
        temp[i] = 0;
    }
}

int main(void) {
    ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
    int T;
    cin >> T;

    // 입력 받기
    for (int i = 0; i < T; ++i) {
        cin >> arr[i];
    }

    reset_arr(T);
    int idx = 1;
    fDp[0] = 1;
    temp[0] = arr[0];
    for (int i = 1; i < T; ++i) {
        bool b = false;

        for (int j = 0; j < idx; ++j) {
            // 비교할려는 대상이 연속된 부분보다 작은 경우에는 해당 값을 집어넣는다
            if (temp[j] >= arr[i]) {
                temp[j] = arr[i];
                b = true;
                break;
            }
        }

        if (b) {
            fDp[i] = fDp[i - 1];
        }
        else {
            temp[idx++] = arr[i];
            fDp[i] = fDp[i - 1] + 1;
        }
    }

    reset_arr(T);
    idx = 1;
    bDp[T - 1] = 1;
    temp[0] = arr[T - 1];
    for (int i = 1; i < T; ++i) {
        int tIdx = T - i - 1;
        bool b = false;

        for (int j = 0; j < idx; ++j) {
            if (temp[j] >= arr[tIdx]) {
                temp[j] = arr[tIdx];
                b = true;
                break;
            }
        }

        if (b) {
            bDp[tIdx] = bDp[tIdx + 1];
        }
        else {
            temp[idx++] = arr[tIdx];
            bDp[tIdx] = bDp[tIdx + 1] + 1;
        }
    }

    int maxValue = 0;
    for (int i = 0; i < T; ++i) {
        if (fDp[i] + bDp[i] - 1 > maxValue) {
            maxValue = fDp[i] + bDp[i] - 1;
        }
    }

    cout << maxValue;
    return 0;
}