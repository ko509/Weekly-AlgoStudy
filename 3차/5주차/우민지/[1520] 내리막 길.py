# https://www.acmicpc.net/problem/1520

'''
알고리즘 : DFS
이유 : (0,0) 에서 (N-1, M-1) 까지 이동하는 모든 경우의 수를 재귀적으로 카운트 해야 함
'''

M, N = map(int, input().split())

board = []

for i in range(M):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dp = [[-1] * N for _ in range(M)]

def dfs(x, y):
    if x == M-1 and y == N-1: # 재귀 함수 탈출 조건
        return 1

    if dp[x][y] != -1: # not visited
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4): # 상하좌우 탐색
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if board[nx][ny] < board[x][y]:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]

print(dfs(0, 0))
