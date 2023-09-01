# https://www.acmicpc.net/problem/17484

N, M = map(int, input().split())
array = []
# 이동 방향
dx = [1, 1, 1]
dy = [-1, 0, 1]

for _ in range(N):
    data = list(map(int, input().split()))
    array.append(data)

min_fuel = int(1e9) # 최소값

# position, 직전 방향
def dfs(i, j, dir, min_fuel, fuel):
    if i == N-1: # 달 도착
        return min(min_fuel, fuel)
    for k in range(3):
        if k != dir:
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                min_fuel = dfs(nx, ny, k, min_fuel, fuel+array[nx][ny])
    return min_fuel

for j in range(M):
    temp = dfs(0, j, -1, min_fuel,array[0][j])
    min_fuel = min(min_fuel, temp)
print(min_fuel)