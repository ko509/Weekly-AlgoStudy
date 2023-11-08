// 2020KB, 0ms
// �õ� Ƚ�� : 1
// ����, ���� ���� �б�

#include <iostream>

#define ull unsigned long long
using namespace std;

int main(void) {
    ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
    ull X, Y, W, S;
    cin >> X >> Y >> W >> S;

    ull ans = 0;
    // �밢������ ���°��� ȿ�������� ���� Ȥ�� ���η� ���°��� ȿ�������� ���
    // ���� Ȥ�� ���η� ���°��� ȿ�����̶��...
    if (W * 2 <= S) {
        ans = (X + Y) * W;
    }
    else {
        // �밢���� ȿ�����̶��...
        // �밢������ �����̴°����� ������ ���� �͵� �� �� �ִ�
        // (0, 0) -> (0, 12)�� �̵��� : (0, 0) -> (6, 6) -> (0, 12)���ε� ������ �� �ֱ� ������ ���� �밢������ �����̰� ������ �κп� ���ؼ��� �Ѻ����� �����̸�ȴ�
        ull zeroToTarget = X > Y ? X - Y : Y - X;
        ans = X > Y ? Y * S : X * S;

        // �Ѻ�Ͼ� �̵��ϴ� ���� ȿ�����̶��
        if (W <= S) {
            ans += zeroToTarget * W;
        }
        else {
            // �밢�� �̵��� ������ ȿ�����̶��
            // ���߿����� ��ĭ�� ���� Ȥ�� ���η� ���������ϴ��� �˻��ؾ��Ѵ�
            ull v1 = (zeroToTarget / 2) * 2;
            ull v2 = zeroToTarget % 2;
            v2 *= W;
            ans += (v1 * S) + v2;
        }
    }

    cout << ans;

    return 0;
}