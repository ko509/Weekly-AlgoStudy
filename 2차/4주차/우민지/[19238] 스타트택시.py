from collections import deque

# https://www.acmicpc.net/problem/19238
N, M, fuel = map(int, input().split())
board = []
flag = False
answer = int(1e9)
customer = []
for _ in range(N):
    board.append(list(map(int, input().split())))
sx, sy = map(int, input().split()) # taxi start position
for _ in range(M):
    ax, ay, bx, by = map(int, input().split())
    customer.append([ax, ay, bx, by])
customer.sort() # 행, 열 순으로 정렬

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 1. 거리가 가장 가까운 손님 구하기
def next_customer(sx, sy):
    distance = [[-1] * N for _ in range(N)] # taxi 좌표에서 모든 칸까지의 거리를 저장
    queue = deque([])
    queue.append((sx, sy))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not distance[nx][ny]:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
    min_dist = int(1e9)
    cx, cy = 0, 0 # next customer 좌표 
    # check customer
    for c in customer:
        ax, ay = c[0], c[1] # 출발지 좌표만 사용 
        if min_dist > distance[ax][ay]:
            min_dist = distance[ax][ay]
            cx, cy = ax, ay
    return cx, cy

# 2. 손님을 출발지에서 목적지로 이동시키기
def move(ax, ay, bx, by):
    # 목적지에서 출발지까지의 거리 구하기
    distance = [[-1] * N for _ in range(N)]

print(next_customer(sx, sy))

if flag:
    print(answer)
else:
    print(-1)