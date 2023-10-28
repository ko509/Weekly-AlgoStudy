def dfs(m,n):
    
    
    if m== M-1 and n == N-1:
        return 1
    
    if DP[m][n] != -1 :
        return DP[m][n]
    
    cnt = 0
    for i in range(4):
        
        if 0<=m+nx[i]<M and 0<=n +ny[i]<N and S[m+nx[i]][n+ny[i]] < S[m][n]:
            
            cnt += dfs(m+nx[i],n+ny[i])
    
    DP[m][n] = cnt
    
    return DP[m][n]
            
            
        




M, N = map(int,input().split())
S = []
DP =[[-1 for _ in range(N)] for _ in range(M)]
nx = [-1,1,0,0]
ny = [0,0,1,-1]
for i in range(M):
    S.append(list(map(int,input().split())))
    


print(dfs(0,0))
