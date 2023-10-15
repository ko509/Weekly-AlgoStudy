def solution(board, skill):
    answer = 0
    N, M = len(board), len(board[0])
    imos = [[0] * (M + 1) for _ in range(N + 1)]
    
    for t, r1, c1, r2, c2, deg in skill:        
        if t == 1:
            deg = -deg
        
        imos[r1][c1] += deg
        imos[r1][c2 + 1] -= deg
        imos[r2 + 1][c1] -= deg
        imos[r2 + 1][c2 + 1] += deg
    
    for i in range(N):
        for j in range(1, M):
            imos[i][j] += imos[i][j - 1]
    
    for i in range(1, N + 1):
        for j in range(M):
            imos[i][j] += imos[i - 1][j]
    
    
    for i in range(N):
        for j in range(M):
            board[i][j] += imos[i][j]
            if board[i][j] > 0:
                answer += 1
                
    return answer
