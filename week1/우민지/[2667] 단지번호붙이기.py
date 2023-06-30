from collections import deque

answer = []

n = int(input())
array = []
visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    array.append(list(map(int, input())))

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
            if 0 <= nx < n and 0 <= ny < n and array[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                count += 1
                queue.append((nx, ny))

    return count

for i in range(n):
    for j in range(n):
        if array[i][j] == 1 and not visited[i][j]:
            answer.append(bfs(i, j))


answer.sort()
print(len(answer))
for a in answer:
    print(a)
