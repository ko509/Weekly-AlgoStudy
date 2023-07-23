# https://www.acmicpc.net/problem/28305

n, t = map(int, input().split())
array = list(map(int, input().split()))
array.sort()  # 3 4 5 6 7
dp = [0] * 200000

print(max(dp))
