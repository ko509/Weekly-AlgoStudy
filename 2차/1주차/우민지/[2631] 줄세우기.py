# https://www.acmicpc.net/problem/2631

answer = int(1e9)

N = int(input())
arr = [0] # index 맞춰주기
for _ in range(N):
    arr.append(int(input()))

dp = [1] * (N+1)

for i in range(1, N+1):
    for j in range(1, i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
# 전체 - 가장 긴 증가하는 수열의 길이
print(N - max(dp))