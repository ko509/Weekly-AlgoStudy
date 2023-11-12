from sys import stdin
from collections import deque
from itertools import combinations
input = stdin.readline

N, M = map(int, input().split())
labs = [list(map(int, input().split())) for _ in range(N)]
virus = []
res = float('inf')

def bfs(v):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    queue = deque(v)
    visited = [[-1] * N for _ in range(N)]
    max_cnt = 0

    for x, y in queue:
        visited[x][y] = 0

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == -1 and labs[nx][ny] != 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[cx][cy] + 1
                    max_cnt = max(max_cnt, visited[cx][cy] + 1)

    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1 and labs[i][j] != 1:
                return float('inf')

    return max_cnt


# 바이러스 좌표 찾기
for i in range(N):
    for j in range(N):
        if labs[i][j] == 2:
            virus.append((i, j))

for v in combinations(virus, M):
    res = min(bfs(v), res)

print(-1 if res == float('inf') else res)
