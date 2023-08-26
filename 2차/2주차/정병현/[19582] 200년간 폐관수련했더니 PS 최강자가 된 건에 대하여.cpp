#include <bits/stdc++.h>
using namespace std;
using pii=pair<int, int>;
int main(){
	cin.tie(0)->sync_with_stdio(0);
	int n, now = 0, t = -1, mex = 0, flag = 3;
	vector<pii> v;
	cin >> n;
	v.resize(n);
	for(auto&[a, b] : v)
		cin >> a >> b;
	for(int i = 0; i < n; i++){
		if(now <= v[i].first){
			now += v[i].second;
			mex = max(v[i].second, mex);
		}
		else if(t == -1){
			t = i;
			now -= mex;
			if(now > v[i].first){
				flag ^= (1<<1);
				break;
			}
			now += v[i].second;
		}
		else{
			flag ^= (1<<1);
			break;
		}
	}
	now = 0;
	for(int i = 0; i < n; i++){
		if(i == t)
			continue;
		if(now > v[i].first){
			flag ^= 1;
			break;
		}
		now += v[i].second;
	}
	cout << (flag?"Kkeo-eok":"Zzz");
}