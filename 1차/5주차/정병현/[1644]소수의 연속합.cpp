#include <bits/stdc++.h>
using namespace std;
using ll=long long;
char p[4000000/8] = {0, };
inline bool is_not_prime(int n){
	return p[n>>3] & (1 << (n & 7));
}

int main(){
	vector<int> primes;
	// bitwise sieve
	for(ll i = 2; i*i < 4000000; i++)
		if(!is_not_prime(i)){
			primes.push_back(i);
			for(ll j = i*i; j < 4000000; j+=i)
				p[j>>3] |= (1 << (j & 7));
		}
	for(ll i = 2000; i < 2000000; i++)
		if(!is_not_prime(i))
			primes.push_back(i);
	int n, m = primes.size(), ans = 0;
	cin >> n;
	ans = (n==4000000?0:(n > 2000000 && !is_not_prime(n)));
	// two pointers
	int l = 0, r = 0, sum = 0;
	while(primes[l] <= n && r <= m){
		if(sum < n){
			sum += primes[r++];
		}
		else if(sum > n){
			sum -= primes[l++];
		}
		else{
			//cout << primes[l] << " " << primes[r-1] << "\n";
			ans++;
			sum -= primes[l++];
		}
	}
	cout << ans;
}