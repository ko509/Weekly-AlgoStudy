# https://www.acmicpc.net/problem/11660
import sys
input = sys.stdin.readline # -> 시간초과 방지

N, M = map(int, input().split())
board = [[0] * (N+1)]

for _ in range(N):
    board.append([0] + list(map(int, input().split())))

# 미리 누적합 구해놓기
for i in range(1, N+1):
    for j in range(1, N):
        board[i][j+1] += board[i][j]

for i in range(1, N):
    for j in range(1, N+1):
        board[i+1][j] += board[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    total = board[x2][y2] - board[x2][y1-1] - board[x1-1][y2] + board[x1-1][y1-1]
    print(total)
