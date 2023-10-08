from sys import stdin
input = stdin.readline

N, M, K = map(int, input().split())
nums = []
sums = [0]

for _ in range(N):
    n = int(input())
    nums.append(n)
    sums.append(sums[-1] + n)

for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:
        diff = c - nums[b - 1]

        for i in range(b, N + 1):
            sums[i] += diff
    elif a == 2:
        print(sums[c] - sums[b - 1])
