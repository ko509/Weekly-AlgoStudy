# https://www.acmicpc.net/problem/11054

N = int(input())
data = list(map(int, input().split()))
# 1. 증가하는 부분 수열 구하기
dp_up = [1] * N

for i in range(N):
    for j in range(i):
        if data[i] > data[j]:
            dp_up[i] = max(dp_up[i], dp_up[j] + 1)
# 2. 감소하는 부분 수열 구하기
dp_down = [1] * N

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if data[i] > data[j]:
            dp_down[i] = max(dp_down[i], dp_down[j]+1)

# 3. 합쳐서 최대 길이 구하기
dp = [0] * N
for i in range(N):
    dp[i] = dp_up[i] + dp_down[i] -1 # 중복 원소 삭제

print("dp_up")
print(dp_up)
print("dp_down")
print(dp_down)
print("DP")
print(dp)

print(max(dp))