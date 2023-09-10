#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string chars="0123456789ABCDEF";
string invert(int i, int n){
    string ret = "";
    while(i){
        ret += chars[i%n];
        i /= n;
    }
    reverse(ret.begin(), ret.end());
    return ret;
}

string solution(int n, int t, int m, int p) {
    string ans = "", tt = "0";
    p--;
    int size = m*t;
    for(int i = 1; i < size;i++)
        tt += invert(i, n);
    while(ans.size() < t){
        ans += tt[p];
        p += m;
    }
    return ans;
}