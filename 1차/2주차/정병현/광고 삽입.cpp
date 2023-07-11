#include <bits/stdc++.h>
using namespace std;
using ll=long long;

string solution(string play_time, string adv_time, vector<string> logs) {
    int n = logs.size();
    char c;
    int h, m, s, ptime, atime;
    stringstream ssin; // use sstream for easy parsing
    vector<int> times, watching;
    string ans = "";
    ///// get playtime
    ssin.str(play_time);
    ssin >> h >> c >> m >> c >> s;
    ssin.clear();
    ptime = 3600*h + 60*m + s;
    
    times.resize(ptime+1);
    watching.resize(ptime+1);
    ///// get advertising time
    ssin.str(adv_time);
    ssin >> h >> c >> m >> c >> s;
    ssin.clear();
    atime = 3600*h + 60*m + s;
    // cout << "ptime : " << ptime << "\n";
    // cout << "atime : " << atime << "\n";
    for(int i = 0; i < n; i++){ // make differentiation array of watching people
        ssin.str(logs[i]);
        ssin >> h >> c >> m >> c >> s >> c;
        times[3600*h + 60*m + s]++;
        ssin >> h >> c >> m >> c >> s;
        ssin.clear();
        times[3600*h + 60*m + s]--;
    }
    watching[0] = times[0];
    //making sumarray
    for(int i = 1; i <= ptime; i++)
        watching[i] = watching[i-1] + times[i];
    // sliding window
    ll max_ad = 0, max_time = 0, now_ad = 0;
    for(int i = 0; i < atime; i++)
        now_ad += watching[i];
    max_ad = now_ad;
    for(int i = 0; i <= ptime - atime; i++){
        now_ad -= watching[i];
        now_ad += watching[i+atime];
        if(now_ad > max_ad){
            max_ad = now_ad;
            max_time = i+1;
            //cout << i << "\n";
        }
    }
    h = max_time / 3600;
    m = (max_time / 60) - 60*h;
    s = max_time % 60;
    if(h < 10)
        ans += "0";
    ans += to_string(h)+":";
    if(m < 10)
        ans += "0";
    ans += to_string(m)+":";
    if(s < 10)
        ans += "0";
    ans += to_string(s);
    return ans;
}
