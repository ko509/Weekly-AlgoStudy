from sys import stdin
from collections import deque, defaultdict
input = stdin.readline

def bfs(k, v):
    queue = deque()
    visited = [0] * (N + 1)

    queue.append(v)
    visited[v] = 1

    cnt = 0
    while queue:
        cur = queue.popleft()

        for i in graph[cur]:
            if not visited[i[0]]:
                if i[1] >= k:
                    queue.append(i[0])
                    cnt += 1
                    visited[i[0]] = 1

    return cnt

N, Q = map(int, input().split())
graph = defaultdict(list)

for _ in range(N - 1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

for _ in range(Q):
    k, v = map(int, input().split())

    print(bfs(k, v))
