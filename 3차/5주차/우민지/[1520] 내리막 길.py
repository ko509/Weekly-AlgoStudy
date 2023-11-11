# https://www.acmicpc.net/problem/1520

'''
알고리즘 : DFS
이유 : (0,0) 에서 (N-1, M-1) 까지 이동하는 모든 경우의 수를 재귀적으로 카운트 해야 함
But, 모든 경우의 수를 카운트 하기 때문에 시간초과 발생
-> 알고리즘 : BFS + DP 사용하여 불필요한 경우를 사전에 제거한다.

'''

M, N = map(int, input().split())

board = []

for i in range(M):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dp = [[-1] * N for _ in range(M)]

def dfs(x, y):
    # 도착 지점에 도달하면 경우의 수가 1 더해진다.
    if x == M-1 and y == N-1: # 재귀 함수 탈출 조건
        return 1
    # 이미 방문한 적 있는 칸이라면 pass (메모이제이션한 값 사용)
    if dp[x][y] != -1:
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
