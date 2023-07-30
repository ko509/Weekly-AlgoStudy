#include <bits/stdc++.h>
using namespace std;
int main(){
	cin.tie(0)->sync_with_stdio(0);
	vector<int> odd, even, pos;
	int n, h, ans = 200200, cnt = 0, a, b;
	cin >> n >> h;
	n>>=1;
	odd.resize(h+1);
	even.resize(h+1);
	for(int i = 0; i < n; i++){
		cin >> a;
		odd[a+1] -= 1;
		cin >> b;
		even[h-b] -= 1;
	}
	odd[1] += n;
	even[h] += n;
	for(int i = 2; i <= h; i++)
		odd[i] += odd[i-1];
	for(int i = h-1; i >= 0; i--)
		even[i] += even[i+1];
	for(int i = 1; i <= h; i++){
		a = odd[i] + even[i];
		//cout << i << " " << odd[i] << " " << even[i] << " " << a << "\n";
		if(ans == a)
			cnt++;
		else if(ans > a){
			ans = a;
			cnt = 1;
		}
	}
	cout << ans << " " << cnt;
}