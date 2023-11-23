#include <iostream>

#define MAX_LEN 31
using namespace std;

int dp[MAX_LEN];

int main(void) {
    ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
    dp[1] = 0;
    dp[2] = 3;

    // 홀수는 dp가 0이다
    for (int i = 4; i <= 30; i += 2) {
        // 기본형태인 
        // ㅡ || =
        // || ㅡ ㅡ 형태 3가지가 기본적으로 2의 배수마다 나타난다.
        dp[i] = dp[i - 2] * 3;
        //   ㅡㅡ
        //   |=| 요런 모양으로 짤라서 할 수 있는 것에 대해서 각 단계마다 경우의 수가 존재한다. 
        // 16을 기준으로 보면 12 4, 10 6, 8, 8 이런식으로 위의 모양을 사용한 형태로 나타낼 수가 있다.
        for (int j = i - 4; j >= 2; j -= 2) {
            dp[i] += dp[j] * 2;
        }
        dp[i] += 2; // 가장 긴 이상한 형태를 더해주어야 한다.
    }

    int N;
    cin >> N;

    cout << dp[N];

    return 0;
}