# https://www.acmicpc.net/problem/2156
N = int(input())
data = [0]
dp = [0] * (N+1) # 누적 포도주 최댓값
for i in range(N):
    data.append(int(input()))
# index 1, 2 의 최댓값
dp[1] = data[1]
if N > 1: # 1 <= N >= 10000
    dp[2] = dp[1] + data[2]
    for i in range(3, N + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + data[i], dp[i - 3] + data[i - 1] + data[i])
        # 1, 2 고르는 경우, 자기 자신은 선택 못함
        # 1, 3 고르는 경우
        # 2, 3 고르는 경우
print(dp[N])