#include <iostream>
#include <map>

#define MAX_LEN 1000001
#define ul unsigned long long
using namespace std;

map<ul, bool> maps;

int main(void) {
    ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);

    ul min_Value, max_Value;
    cin >> min_Value >> max_Value;

    for (ul i = 2; i < MAX_LEN; ++i) {
        ul v = i * i;
        ul s = min_Value / v;
        for (ul j = s; j * v <= max_Value; ++j) {
            map<ul, bool>::iterator iter = maps.find(j * v);
            if (iter == maps.end()) {
                maps.insert(make_pair(j * v, true));
            }
        }
    }

    // 최대 1백만개만 순회하면 되므로 가능
    int cnt = 0;
    for (ul i = min_Value; i <= max_Value; ++i) {
        map<ul, bool>::iterator iter = maps.find(i);
        if (iter == maps.end()) {
            ++cnt;
        }
    }

    cout << cnt;

    return 0;
}