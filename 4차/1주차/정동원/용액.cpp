// 2800KB, 12ms
// �õ� Ƚ�� : 1ȸ
// �̺� Ž��, ��������

#include <iostream>

#define ll long long
#define MAX_LEN 100000
#define MAXVALUE 2000000001
using namespace std;

ll arr[MAX_LEN];

int main(void) {
    ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
    // ��ü ����� ���� �Է¹ޱ�
    int N;
    cin >> N;

    // ����� �Է¹޴´�
    for (int i = 0; i < N; ++i) {
        ll a;
        cin >> a;
        arr[i] = a;
    }

    // ó���� ���� ���� �ε���
    int s = 0;
    int e = N - 1;
    int tS = s, tE = e; // ���� ������ ����(0�� �����) ���� ����� �ε��� ����

    int minValue = MAXVALUE;
    while (s != e) {
        ll v = arr[s] + arr[e];

        // �������� ���� ���� ���� ����Ѵ�.
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