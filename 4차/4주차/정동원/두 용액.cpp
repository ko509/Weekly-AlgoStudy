#include <iostream>
#include <algorithm>

#define MAX_LEN 100000
#define ll long long
using namespace std;

ll arrValue[MAX_LEN];

int main(void) {
    ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
    int N;
    cin >> N;

    for (int i = 0; i < N; ++i) {
        cin >> arrValue[i];
    }


    sort(arrValue, arrValue + N); // 오름차순 정렬

    int s = 0;
    int e = N - 1;

    int rS = s;
    int rE = e;

    ll curValue = 0;
    ll maxValue = 10000000000;

    while (s < e) {
        curValue = arrValue[s] + arrValue[e];
        ll absValue = curValue < 0 ? curValue * (-1) : curValue;

        if (maxValue > absValue) {
            maxValue = absValue;
            rS = s;
            rE = e;
        }

        if (curValue < 0) {
            ++s;
        }
        else {
            --e;
        }
    }

    cout << arrValue[rS] << " " << arrValue[rE];

    return 0;
}