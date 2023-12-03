from sys import stdin
from collections import deque, defaultdict
input = stdin.readline

N, M = map(int, input().split())

singer_info = defaultdict(int)
graph = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)

# 그래프 초기화
for _ in range(M):
    line = list(map(int, input().split()))

    for s in range(1, line[0]):
        graph[line[s]].append(line[s + 1])
        degree[line[s + 1]] += 1  # 노드별 차수 설정

queue = deque()
res = []

# 차수가 0인 노드부터 출력
for i in range(1, N + 1):
    if degree[i] == 0:
        queue.append(i)

# 위상 정렬
while queue:
    node = queue.popleft()
    res.append(node)

    for nxt in graph[node]:
        degree[nxt] -= 1

        if degree[nxt] == 0:
            queue.append(nxt)

if len(res) != N:
    print(0)
else:
    for n in res:
        print(n)

