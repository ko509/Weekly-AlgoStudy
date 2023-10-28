import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

pre_sum = [[0] * (n + 1) for _ in range(n +  1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        pre_sum[i][j] = pre_sum[i][j - 1] + pre_sum[i - 1][j] + graph[i - 1][j - 1] - pre_sum[i - 1][j - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(pre_sum[x2][y2] - pre_sum[x2][y1 - 1] - pre_sum[x1 - 1][y2] + pre_sum[x1 - 1][y1 - 1])
    
#sys 안 쓰면 시간초과.............