from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
modCnts = [0] * M
sums = 0

for i in range(N):
    sums += nums[i]
    modCnts[sums % M] += 1

res = modCnts[0]
for c in modCnts:
    res += c * (c - 1) // 2

print(res)
