// 2020KB, 0ms
// 시도 횟수 : 1
// 수학, 많은 조건 분기

#include <iostream>

#define ull unsigned long long
using namespace std;

int main(void) {
    ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
    ull X, Y, W, S;
    cin >> X >> Y >> W >> S;

    ull ans = 0;
    // 대각선으로 가는것이 효율적인지 가로 혹은 세로로 가는것이 효율적인지 계산
    // 가로 혹은 세로로 가는것이 효율적이라면...
    if (W * 2 <= S) {
        ans = (X + Y) * W;
    }
    else {
        // 대각선이 효율적이라면...
        // 대각선으로 움직이는것으로 다음과 같은 것도 할 수 있다
        // (0, 0) -> (0, 12)로 이동시 : (0, 0) -> (6, 6) -> (0, 12)으로도 움직일 수 있기 때문에 전부 대각선으로 움직이고 나머지 부분에 대해서만 한블럭으로 움직이면된다
        ull zeroToTarget = X > Y ? X - Y : Y - X;
        ans = X > Y ? Y * S : X * S;

        // 한블록씩 이동하는 것이 효율적이라면
        if (W <= S) {
            ans += zeroToTarget * W;
        }
        else {
            // 대각선 이동이 여전히 효율적이라면
            // 이중에서도 한칸을 가로 혹은 세로로 움직여야하는지 검사해야한다
            ull v1 = (zeroToTarget / 2) * 2;
            ull v2 = zeroToTarget % 2;
            v2 *= W;
            ans += (v1 * S) + v2;
        }
    }

    cout << ans;

    return 0;
}