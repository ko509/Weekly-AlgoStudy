# https://www.acmicpc.net/problem/13549
from collections import deque

INF = int(1e9)
MAX = 100001
N, K = map(int, input().split())

distance = [INF] * MAX # 시간 기록하기
visited = [False] * MAX # 방문 처리
queue = deque([N])
distance[N] = 0 # 출발할 때 시간
visited[N] = True

while queue:
    now = queue.popleft()
    if 0 <= (now*2) < MAX and not visited[now*2]:
        if distance[now] < distance[now*2]:
            distance[now*2] = distance[now]
            queue.append(now * 2)
    if 0 <= (now+1) < MAX and not visited[now+1]:
        if distance[now+1] > distance[now] + 1:
            distance[now+1] = distance[now] + 1
            queue.append(now+1)
    if 0 <= (now-1) < MAX and not visited[now-1]:
        if distance[now-1] > distance[now] + 1:
            distance[now-1] = distance[now]+1
            queue.append(now-1)

print(distance[K])
