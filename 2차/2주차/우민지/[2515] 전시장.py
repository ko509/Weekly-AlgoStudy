# # https://www.acmicpc.net/problem/2515

N, S = map(int, input().split())

answer = 0 # 최대합
array = [[0,0]]
dp = [0] * (N+1) # i ~ N 번째 중 최대합 금액 저장
height = [0] * (N+1) # i번째 그림을 전시한다고 할 때, 앞에 전시할 수 있는 가장 높은 그림
# S 간격보다 같거나 커야 함 !

for i in range(N):
    H, C = map(int, input().split())
    array.append([H, C])
array.sort()

for i in range(1, N+1):
    height[i] = height[i-1] + 1
    while height[i] < i:
        if array[i][0] - array[height[i]][0] < S:
            break
        height[i] += 1
    height[i] -= 1

# print("height:", height)
for i in range(1, N+1):
    dp[i] = max(dp[i-1], dp[height[i]] + array[i][1])
# print("dp:", dp)
print(dp[N])



