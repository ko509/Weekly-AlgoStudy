#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, int s) {
    vector<int> ans;
    if(s/n == 0)
        ans.push_back(-1);
    else{
        for(int i = 0; i < n-s%n; i++)
            ans.push_back(s/n);
        for(int i = 0; i < s%n; i++)
            ans.push_back(s/n + 1);
    }
    return ans;
}