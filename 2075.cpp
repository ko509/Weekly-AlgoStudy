#include <bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(0); cin.tie(0);
	vector<int> v;
	int n;
	cin >> n;
	v.resize(n*n);
	for(int i = 0; i < n*n; i++)
		cin >> v[i];
	//nth_element(v.begin(), v.begin()+(n-1), v.end(), greater<int>());
	sort(v.begin(), v.end(), greater<int>());
	cout << v[(n-1)];
}