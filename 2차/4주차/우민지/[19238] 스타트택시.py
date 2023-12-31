from collections import deque
N, M, fuel = map(int, input().split()) # fuel = 15
board = []
flag = True

customer = []
for _ in range(N):
    board.append(list(map(int, input().split())))
sx, sy = map(int, input().split()) # taxi start position
sx -= 1 # board 랑 index 맞추기
sy -= 1

for _ in range(M):
    ax, ay, bx, by = map(int, input().split())
    customer.append([ax-1, ay-1, bx-1, by-1])
customer.sort() # 행, 열 순으로 정렬

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 1. 거리가 가장 가까운 손님 구하기
def next_customer():
    global fuel, sx, sy, flag
    distance = [[-1] * N for _ in range(N)] # taxi 좌표에서 모든 칸까지의 거리를 저장
    queue = deque([])
    queue.append((sx, sy))
    distance[sx][sy] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 1 and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

    min_dist = int(1e9)
    next_cus = [0, 0, 0, 0] # next customer 좌표
    # check customer
    for c in customer:
        ax, ay, bx, by = c[0], c[1], c[2], c[3] # 출발지 좌표만 사용
        if min_dist > distance[ax][ay]:
            min_dist = distance[ax][ay]
            next_cus = [ax, ay, bx, by]
    if min_dist == -1 or min_dist == int(1e9):
        print(-1)
        exit()
    # Fuel Check
    if fuel < min_dist:
        flag = False
        print(-1)
        exit()
    else:
        fuel -= min_dist
        sx, sy = next_cus[0], next_cus[1]

    return next_cus

# 2. 손님을 출발지에서 목적지로 이동시키기
def move(ax, ay, bx, by):
    # 목적지에서 출발지까지의 거리 구하기
    distance = [[-1] * N for _ in range(N)]
    distance[ax][ay] = 0
    queue = deque([])
    queue.append((ax, ay))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 1 and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
    return distance[bx][by] # dist



while customer:
    c = next_customer()
    dist = move(c[0], c[1], c[2], c[3])
    if fuel >= dist: # 손님 이동시키기 성공 한 경우
        fuel += dist
        sx, sy = c[2], c[3] # 손님의 목적지가 택시의 새로운 출발지점이 된다.
    else:
        flag = False
        print(-1)
        exit()
        break
    # 삭제하기
    customer.remove(c)
    customer.sort()

if flag:
    print(fuel)
else:
    print(-1)