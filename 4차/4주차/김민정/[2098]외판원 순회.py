from sys import stdin
input = stdin.readline

N = int(input())
cities = [list(map(int, input().split())) for _ in range(N)]
INF = int(1e9)
dp = {}

def dfs(now, visited):
    if visited == (1 << N) - 1:
        if cities[now][0]:
            return cities[now][0]
        else:
            return INF

    if (now, visited) in dp:
        return dp[(now, visited)]

    min_cost = INF
    for nxt in range(1, N):
        if cities[now][nxt] == 0 or visited & (1 << nxt):
            continue

        cost = dfs(nxt, visited | (1 << nxt)) + cities[now][nxt]
        min_cost = min(cost, min_cost)

    dp[(now, visited)] = min_cost
    return min_cost

print(dfs(0, 1))
