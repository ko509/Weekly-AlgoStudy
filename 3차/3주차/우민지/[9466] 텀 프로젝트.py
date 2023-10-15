# https://www.acmicpc.net/problem/9466
import sys
sys.setrecursionlimit(10**6)

def dfs(node):
    global data, visited, cycle
    visited[node] = True
    cycle.append(node)
    if visited[data[node]]: # 이미 방문 했으면
        if data[node] in cycle:
            team.extend(cycle[cycle.index(data[node]):])
    else:
        dfs(data[node])


T = int(input())
for _ in range(T):
    N = int(input()) # 학생의 수
    visited = [False] * (N+1)
    data = [0] + list(map(int, input().split()))
    edge = [[] for _ in range(N+1)]
    team = [] # 팀에 속하게 된 학생 목록

    for i in range(1, N+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    # 팀에 속하지 못한 학생 수
    print(N - len(team))