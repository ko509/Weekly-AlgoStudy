#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
int n;
vector <int> sum[2005];
vector <int> num;
void input()
{
	int t;
	cin >> n;
	for (int i = 0; i < n; i++) {
	    cin >> t;
		num.push_back(t);
	}
}
int solve()
{
	if (n <= 2) {
		return 0;
	}
	sort(num.begin(), num.end());
	int number = 0;
	for (auto i : num) {
		number += i;
	}
	if (number == 0) {
		return n;
	}
	for (int i = 2; i < n; i++) {

		for (int j = 0; j < i; j++) {
			if (i-2 == j) continue;
			int x = num[i-2] + num[j];

			sum[i].push_back(x); // sum[i]는 i를 포함한 구간 i~n까지의 합
		}
		sort(sum[i].begin(), sum[i].end());
	}
	int res = 0;

	for (int i = n-1; i >= 0; i--) {
		for (int j = 0; j <= i; j++) {

			auto t = lower_bound(sum[j].begin(), sum[j].end(), num[i]);

			if (lower_bound(sum[j].begin(), sum[j].end(), num[i]) != sum[j].end()) {
				if (*t > num[i]) {
					continue;
				}
				res++;
				break;
			}
		}
	}
	return res;
}

int main()
{
	cin.tie(0); 
	ios::sync_with_stdio(0);
	input();
	cout << solve();
}
