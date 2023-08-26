#include <bits/stdc++.h>
using namespace std;
using pii=pair<int, int>;
using ll=long long;
char c;
ll n, s, w, g, r, I, d1, d2, t, pos;
vector<int> land, state;
vector<pii> gold;
int main(){
	cin.tie(0)->sync_with_stdio(0);
	cin >> n >> s >> w >> g;
	t = 4*n-4;
	land.resize(t);
	state.resize(t);
	gold.resize(g);
	int tt = n-1;
	for(auto&[a, b] : gold)
		cin >> a >> b;
	for(int i = 1; i < t; i++){
		if(i == tt){
			i++;
			tt += n-1;
		}
		cin >> c;
		if(c == 'G'){
			land[i] = -1;
			//state[i] = 1;
		}
		else{
			cin >> d1;
			land[i] = d1;
		}
	}
	
	pos = 0;
	int en = 0;
//	for(int i : land)
//		cout << i << "\n";
//	for(auto[a, b] : gold)
//		cout << a << " " << b << "\n";
	cin >> I;
	while(I--){
		cin >> d1 >> d2;
		pos += d1 + d2;
		while(pos >= t){
			s += w;
			pos -= t;
		}
//		cout << pos << " " << s << "\n";
//			for golden key cards
		if(land[pos] == -1){
			switch(gold[en].first){
				case 1:
					s += gold[en].second;
					break;
				case 2:
					s -= gold[en].second;
					if(s < 0){
						cout << "LOSE";
						return 0;
					}
					break;
				case 3:
					s -= gold[en].second;
					r += gold[en].second;
					if(s < 0){
						cout << "LOSE";
						return 0;
					}
					break;
				case 4:
					pos += gold[en].second;
					break;
			}
			en++;
			if(en >= g)
				en -= g;
//			cout << pos << " " << s << "\n";
		}
//			after golden key, pass the start position
		while(pos >= t){
			s += w;
			pos -= t;
		}
//  		another 
		if(land[pos] == 0){
			int pp = pos / (n-1);
			if(pp == 1){
				for(int i = 0; i < 3; i++){
					if(I <= 0)
						break;
					I--;
					cin >> d1 >> d2;
					if(d1 == d2)
						break;
				}
			}
			else if(pp == 2){
				s += r;
				r = 0;
			}
			else if(pp == 3){
				pos = 0;
				s += w;
			}
		}
		else if(land[pos] > 0){
			if(state[pos] == 1)
				continue;
			if(s < land[pos])
				continue;
			s -= land[pos];
			state[pos] = 1;
		}
	}
	
	// check whether win or not
	int flag = 1;
	for(int i = 1; i < t; i++){
		if(land[i] == 0 || land[i] == -1)
			continue;
		if(state[i] == 0){
			flag = 0;
			break;
		}
	}
	for(int i = 0; i < t; i++)
		cout << state[i] << " ";
	cout << (flag?"WIN":"LOSE");
}