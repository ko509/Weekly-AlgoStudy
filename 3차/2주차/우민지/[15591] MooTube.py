# https://www.acmicpc.net/problem/15591
from collections import deque
import sys

input = sys.stdin.readline
N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
INF = int(1e9)
for _ in range(N-1): # edge 정보
    p, q, r = map(int, input().split())
    graph[p].append([q, r])
    graph[q].append([p, r])

def solve(K, V):
    result = 0 # K 이상인 영상 개수
    visited = [False] * (N+1)
    queue = deque([[V, INF]]) # node, usado
    visited[V] = True
    while queue:
        now, now_usado = queue.popleft()
        for next, next_usado in graph[now]:
            next_usado = min(now_usado, next_usado)
            if not visited[next] and next_usado >= K:
                result += 1
                visited[next] = True
                queue.append([next, next_usado])
    return result

# v 와 유사도가 K 이상인 동영상 개수 구하기
for _ in range(Q):
    k, v = map(int, input().split())
    print(solve(k, v))