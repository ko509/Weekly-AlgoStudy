from collections import deque
from itertools import combinations

N, M = map(int, input().split())

board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
wall_cnt = 0 # 벽의 개수

INF = int(1e9)
answer = INF
virus_pos = [] # virus 를 둘 수 있는 칸의 위치 저장
for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        if data[j] == 2:
            virus_pos.append([i, j])

    wall_cnt += data.count(1)
    board.append(data)

# virus 가 모두 퍼졌는지 확인
def check_virus(arr):
    cnt = 0
    for i in range(N):
        cnt += arr[i].count(-1)
    if cnt == wall_cnt:
        return True
    else:
        return False

def bfs(case):
    queue = deque([])
    visited = [[-1] * N for _ in range(N)]
    time_cnt = 0

    for x, y in case:
        queue.append((x, y))
        visited[x][y] = 0 # virus 감염된 칸, virus 배치는 0 초에서 시작 ?

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 1 and visited[nx][ny] == -1:
                queue.append((nx, ny)) # 새로 바이러스가 퍼진 칸
                visited[nx][ny] = visited[x][y] + 1 # 바이러스 방문 처리 &확산 된 시간
                time_cnt = max(time_cnt, visited[nx][ny])
    # print(visited)
    if check_virus(visited):
        return time_cnt
    else:
        return INF


# virus 를 배치하는 모든 경우의 수
virus_case = list(combinations(virus_pos, M))

for case in virus_case:
    answer = min(bfs(case), answer)

if answer == INF:
    print(-1)
else:
    print(answer)
