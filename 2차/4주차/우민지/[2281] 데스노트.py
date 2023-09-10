# https://www.acmicpc.net/problem/2281

n, m = map(int, input().split())
name = [] # 7, 4, 2, 3, 2, 5, 1, 12, 7, 5, 6
answer = int(1e9) # 남게 되는 칸의 수의 제곱의 합이 최소가 되도록 한다
for _ in range(n):
    name.append(int(input()))

print(answer)