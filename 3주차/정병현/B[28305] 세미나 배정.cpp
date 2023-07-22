#include <bits/stdc++.h>
using namespace std;
using ll=long long;
int check(int m, int T, vector<int>& v){ // can it possible to fit in m classes?
	int n = v.size();
	for(int i = 0; i < m; i++){
		int endtime = 0;
		for(int j = i; j < n; j+=m){
			if(endtime >= v[j]){
				//cout << endtime << " " << v[j] << "\n";
				return 0;
			}
			endtime += T;
			endtime = max(endtime, v[j]);
		}
	}
	return 1;
}
int main(){
	int n, t, l, r, m;
	vector<int> v;
	cin >> n >> t;
	v.resize(n);
	for(auto& i : v)
		cin >> i;
	sort(v.begin(), v.end());
//	for(auto i : v)
//		cout << i << " ";
//	cout << "\n";
	l = 0; r = n+1; m=(l+r)>>1;
	while(l+1 < r){ // binary search
		int T = check(m, t, v);
		//cout << l << " " << m << " " << r << " " << T << "\n";
		if(T)
			r = m;
		else
			l = m;
		m = l+r>>1;
	}
	cout << r;
}