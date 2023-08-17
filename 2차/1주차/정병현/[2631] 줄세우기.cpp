#include <bits/stdc++.h>
using namespace std;
int main(){
	int n;
	vector<int> v, last;
	cin >> n;
	v.resize(n);
	for(int& i : v)
		cin >> i;
	//lis
	for(int i = 0; i < n; i++){
		auto it = lower_bound(last.begin(), last.end(), v[i]);
		if(it == last.end())
			last.push_back(v[i]);
		else if(*it > v[i])
			*it = v[i];
	}
	cout << n - last.size();
}