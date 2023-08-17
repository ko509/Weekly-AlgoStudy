#include <bits/stdc++.h>
using namespace std;
using pii=pair<int, int>;
vector<pii> v;
int n;
// proceed left side
int left(int l, int x){ // get max idx and x value
	if(l == -1)
		return 0;
	int t = 0;
	for(int i = 1; i <= l; i++){
		if(v[t].second < v[i].second)
			t = i;
	}
	int tans = left(t-1, v[t].first) + v[t].second*(x - v[t].first);
//	cout << "  " << v[t].first << " " << tans << " " << v[t].second*(x - v[t].first) << "\n";
	return tans;
}
// proceed right side
int right(int r, int x){ // get min idx and x value
	if(r == n)
		return 0;
	int t = r;
	for(int i = r+1; i < n; i++){
		if(v[t].second <= v[i].second)
			t = i;
	}
	int tans = right(t+1, v[t].first) + v[t].second*(v[t].first - x);
//	cout << "  " << v[t].first << " " << tans << " " << v[t].second*(v[t].first - x) << "\n";
	return tans;
}
int main(){
	cin >> n;
	v.resize(n);
	for(auto&[x, y] : v)
		cin >> x >> y;
	sort(v.begin(), v.end());
	int l, r; // if there is multiple longest pillar
	l = r = 0;
	for(int i = 1; i < n; i++){
		if(v[r].second < v[i].second)
			l = r = i;
		else if(v[r].second == v[i].second)
			r = i;
		//cout << l << " " << r << "\n";
	}
	int ans = left(l-1, v[l].first) + right(r+1, v[r].first) + (v[r].first - v[l].first + 1)*v[l].second;
	//cout << v[l].first << " " << v[r].first << "\n";
	cout << ans;
}