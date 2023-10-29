# https://www.acmicpc.net/problem/1261
from collections import deque

M, N = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

board = [list(map(int, input())) for _ in range(N)]

queue = deque()
queue.append([0, 0]) # x, y

# 벽 부신 횟수 저장하기
distance = [[-1] * M for _ in range(N)]
distance[0][0] = 0
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and distance[nx][ny] == -1:

            if board[nx][ny] == 0: # 통로 -> 가중치가 더 높으므로 appendleft
                distance[nx][ny] = distance[x][y]
                queue.appendleft([nx, ny])
            else: # 벽 -> 가중치가 낮으므로 append (right)
                distance[nx][ny] = distance[x][y] + 1
                queue.append([nx, ny])


print(distance[N-1][M-1])