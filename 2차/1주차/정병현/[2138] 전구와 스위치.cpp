#include<bits/stdc++.h>
using namespace std;
int main(){
	int n;
	cin >> n;
	string sans, scopy;
	vector<int> ans(n), copy(n), input(n);
	cin >> sans;
	cin >> scopy;
	for(int i = 0; i < n; i++){
		ans[i] = sans[i]-48;
		copy[i] = scopy[i]-48;
	}
	input = copy;
	int tans = 0, ttans = 1;
	// if do not toggle [0]
	for(int i = 1; i < n-1; i++){
		if(ans[i-1] ^ input[i-1]){ //if they are different, toggle it and those around it
			input[i-1]^=1;
			input[i]^=1;
			input[i+1] ^= 1;
			tans++;
		}
//  		for(int i = 0; i < n; i++)
//  	  		cout << input[i];
//  		cout << "\n";
	}
	if((input[n-2] ^ ans[n-2]) ^ (input[n-1]^ans[n-1])){
		tans += (input[n-1] != ans[n-1]);
	}
	else
		tans = -1;
		
	//if toggle [0]
	input = copy;
	input[0] ^= 1;
	input[1] ^= 1;
	for(int i = 1; i < n-1; i++){
		if(ans[i-1] ^ input[i-1]){
			input[i-1] ^= 1;
			input[i] ^= 1;
			input[i+1] ^= 1;
			ttans++;
		}
//		for(int i = 0; i < n; i++)
//			cout << input[i];
//		cout << "\n";
	}
	if((input[n-2] ^ ans[n-2]) ^ (input[n-1]^ans[n-1])){
		ttans += (input[n-1] != ans[n-1]);
	}
	else
		ttans = -1;
	
	if(tans == -1 && ttans == -1)
		cout << "-1";
	else if(tans == -1 || ttans == -1)
		cout << max(tans, ttans);
	else
		cout << min(tans, ttans);
}