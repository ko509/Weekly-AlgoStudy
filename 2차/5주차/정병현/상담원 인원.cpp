#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> teachers;

void make_combinations(int remain, int idx, vector<int>& teacher){
    if(remain <= 0){
        teachers.push_back(teacher);
        return;
    }
    
    for(int i = idx; i < teacher.size(); i++){
        teacher[i]++;
        make_combinations(remain-1,i,teacher);
        teacher[i]--;
    }
}

int simulation(vector<int>& teacher, vector<vector<int>>& reqs){
    priority_queue<int,vector<int>, greater<int>> pq[teacher.size()];
    int result = 0;
    
    for(int i = 1; i < teacher.size(); i++)
        for(int j = 0; j < teacher[i]; j++)
			pq[i].push(0);
    
    for(auto req : reqs){
        int arrive = req[0];
        int time = req[1];
        int idx = req[2];
        
        int picked = pq[idx].top();
        pq[idx].pop();
        
        if(picked > arrive){
            result += picked-arrive;
            pq[idx].push(picked+time);
        }
        else if(picked < arrive)
			pq[idx].push(arrive+time);
        else
			pq[idx].push(picked+time);
    }
    
    return result;
}
int solution(int k, int n, vector<vector<int>> reqs) {
    int answer = 2147483647;
    
    vector<int> teacher(k+1,1);
    make_combinations(n-k,1,teacher);
    
    for(auto teacher : teachers)
        answer = min(answer,simulation(teacher,reqs));
    
    return answer;
}