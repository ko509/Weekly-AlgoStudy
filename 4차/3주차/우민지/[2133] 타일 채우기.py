# https://www.acmicpc.net/problem/2133

N = int(input())

dp = [0] * 31
dp[2] = 3

for i in range(4, 31):
    if i % 2 == 0: # 짝수
        dp[i] = dp[i-2] * 3 + 2 + sum(dp[:i-2]) * 2# 특이한 모양 2개
    else:
        dp[i] = 0

print(dp[N])