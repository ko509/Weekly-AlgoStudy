#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

vector<int> solution(string msg) {
    vector<int> answer;
    map<string, int> mp; // map for string and value of that string
    int n = msg.size(), mps, i = 0;
    string s = " ";
    s[0]+=33;
    for(char i = 1; i <= 26; i++){
        mp[s] = i;
        s[0]++;
    }
    s = "";
    mps = 26; // mps means size of mp
    while(i < n){
        s+=msg[i];
        //cout << i << " " << s << "\n";
        if(mp[s]){
            i++;
            continue;
        }
        mp[s] = ++mps;
        s.pop_back();
        answer.push_back(mp[s]);
        s = "";
    }
    if(s != "")
        answer.push_back(mp[s]);
    return answer;
}
