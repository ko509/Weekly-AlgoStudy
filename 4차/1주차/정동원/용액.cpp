// 2800KB, 12ms
// 시도 횟수 : 1회
// 이분 탐색, 투포인터

#include <iostream>

#define ll long long
#define MAX_LEN 100000
#define MAXVALUE 2000000001
using namespace std;

ll arr[MAX_LEN];

int main(void) {
    ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
    // 전체 용액의 개수 입력받기
    int N;
    cin >> N;

    // 용액을 입력받는다
    for (int i = 0; i < N; ++i) {
        ll a;
        cin >> a;
        arr[i] = a;
    }

    // 처음과 끝에 대한 인덱싱
    int s = 0;
    int e = N - 1;
    int tS = s, tE = e; // 가장 오차가 적은(0과 가까운) 수를 기억할 인덱싱 변수

    int minValue = MAXVALUE;
    while (s != e) {
        ll v = arr[s] + arr[e];

        // 오차값이 가장 적은 것은 기억한다.
        if (abs(v) < minValue) {
            minValue = abs(v);
            tS = s;
            tE = e;
        }

        if (v < 0) {
            ++s;
        }
        else {
            --e;
        }
    }

    cout << arr[tS] << " " << arr[tE];

    return 0;
}