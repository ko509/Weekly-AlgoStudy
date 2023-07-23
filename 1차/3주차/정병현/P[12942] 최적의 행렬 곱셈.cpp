#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> matrix_sizes) {
    vector<int> sizes;
    vector<vector<int>> ans;
    sizes.resize(matrix_sizes.size()+1);
    int n = 0;
    for(auto& i : matrix_sizes)
        sizes[n++] = i[0];
    sizes[n] = matrix_sizes[n-1][1];
    ans.resize(n);
    for(int i = 0; i < n; i++){ // setting dp table
        ans[i].resize(n, 700000000);
        ans[i][i] = 0;
    }
        
    for(int k = 1; k < n; k++){ // dp
        for(int i = 0; i+k < n; i++){
            for(int j = i; j < i+k; j++){
                ans[i][i+k] = min(ans[i][i+k], ans[i][j] + ans[j+1][i+k] + sizes[i]*sizes[j+1]*sizes[i+k+1]);
            }
        }
    }
    // for(int i : sizes)
    //     cout << i << " ";
    // cout << "\n";
    // for(int i = 0; i < n; i++){
    //     for(int j = 0; j < n; j++)
    //         cout << ans[i][j] << " ";
    //     cout << "\n";
    // }
    return ans[0][n-1];
}