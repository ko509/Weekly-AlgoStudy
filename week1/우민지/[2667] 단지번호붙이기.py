from collections import deque

answer = []

n = int(input())
array = []
visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    array.append(list(map(int, input().split())))

def bfs(sx, sy):

    queue = deque([])
    queue.append((sx, sy))
    visited[sx][sy] = True
    count = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                count += 1
                queue.append((nx, ny))

    return count

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt = bfs(i, j)
            if cnt > 0:
                answer.append(cnt)


answer.sort()
for a in answer:
    print(a)
