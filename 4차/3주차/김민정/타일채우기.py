from sys import stdin
input = stdin.readline

n = int(input())
res = 0

dp = [0] * 31
dp[2] = 3

for i in range(4, n + 1):
    if i % 2 == 0:  # n이 짝수일때만 타일 채우기 가능
        dp[i] += dp[i - 2] * dp[2]

        for j in range(i - 4, -1, -2):
            dp[i] += dp[j] * 2

        dp[i] += 2

print(dp[n])
