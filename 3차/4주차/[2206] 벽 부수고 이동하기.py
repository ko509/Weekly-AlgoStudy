# https://www.acmicpc.net/problem/2206
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy):
    queue = deque([(sx, sy, 0)]) #
    visited = [[[-1] * 2 for _ in range(M)] for _ in range(N)] # -1 이면 not visited , 0 이상은 distance 값 저장
    visited[sx][sy][0] = 1 # flag == 0 or flag == 1
    while queue:
        x, y, flag = queue.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][flag]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny][flag] == -1 and board[nx][ny] == 0: # 이동 가능한 경우
                    visited[nx][ny][flag] = visited[x][y][flag] + 1
                    queue.append([nx, ny, flag]) # flag 는 동일하게 주기
                if board[nx][ny] == 1 and flag == 0: # 벽을 만난 경우
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))
    return -1

print(bfs(0, 0))
