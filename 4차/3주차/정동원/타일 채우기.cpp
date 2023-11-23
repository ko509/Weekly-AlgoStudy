#include <iostream>

#define MAX_LEN 31
using namespace std;

int dp[MAX_LEN];

int main(void) {
    ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
    dp[1] = 0;
    dp[2] = 3;

    // Ȧ���� dp�� 0�̴�
    for (int i = 4; i <= 30; i += 2) {
        // �⺻������ 
        // �� || =
        // || �� �� ���� 3������ �⺻������ 2�� ������� ��Ÿ����.
        dp[i] = dp[i - 2] * 3;
        //   �Ѥ�
        //   |=| �䷱ ������� ©�� �� �� �ִ� �Ϳ� ���ؼ� �� �ܰ踶�� ����� ���� �����Ѵ�. 
        // 16�� �������� ���� 12 4, 10 6, 8, 8 �̷������� ���� ����� ����� ���·� ��Ÿ�� ���� �ִ�.
        for (int j = i - 4; j >= 2; j -= 2) {
            dp[i] += dp[j] * 2;
        }
        dp[i] += 2; // ���� �� �̻��� ���¸� �����־�� �Ѵ�.
    }

    int N;
    cin >> N;

    cout << dp[N];

    return 0;
}