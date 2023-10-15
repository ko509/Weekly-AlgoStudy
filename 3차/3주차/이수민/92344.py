def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    S = [[0 for _ in range(M+1)] for _ in range(N+1)]
    for type, r1, c1, r2, c2, degree in skill:
        
        S[r1][c1] += -degree if type ==1 else degree 
        S[r1][c2+1] += degree if type ==1 else -degree
        S[r2+1][c1] += degree if type ==1 else -degree 
        S[r2+1][c2+1] += -degree if type ==1 else degree
        
    for i in range(N):
        for j in range(M):
            S[i][j+1] += S[i][j]
    for j in range(M):
        for i in range(N):
            S[i+1][j] += S[i][j]
            
            
    for i in range(N):
        for j in range(M):
            board[i][j] += S[i][j]
            if board[i][j] > 0: answer+=1
        
    
    return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))


#이건 못푼문제 확정... 너무 어렵다..