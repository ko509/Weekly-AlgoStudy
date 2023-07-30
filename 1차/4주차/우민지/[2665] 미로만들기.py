# 미로 만들기
import heapq

n = int(input())
array = []
INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

distance = [[INF] * n for _ in range(n)]

for i in range(n):
    array.append(list(map(int, input())))

def solve(sx, sy): # start
    queue = []
    heapq.heappush(queue, (0, sx, sy)) # black_cnt, x, y
    distance[sx][sy] = 0
    while queue:
        b_cnt, x, y = heapq.heappop(queue)

        if b_cnt > distance[x][y]: # 이미 처리된 값
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                new_cnt = b_cnt
                if array[nx][ny] == 0: # if it's black room
                    new_cnt += 1
                if new_cnt < distance[nx][ny]:
                    distance[nx][ny] = new_cnt # nx, ny 까지의 검은방 count 기록
                    heapq.heappush(queue, (new_cnt, nx, ny))

solve(0, 0)

print(distance[-1][-1])