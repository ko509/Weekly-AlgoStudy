from sys import stdin
input = stdin.readline

N = int(input())

wine = [0]

for _ in range(N):
    wine.append(int(input()))

dp = [0, wine[1]]

if N > 1:
    dp.append(wine[1] + wine[2])

for i in range(3, N + 1):
    dp.append(max(dp[i - 1], dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i]))

print(dp[N])
