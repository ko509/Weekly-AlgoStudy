# https://www.acmicpc.net/problem/2042

N, M, K = map(int, input().split())
data = []

for _ in range(N):
    data.append(int(input()))

for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        data[b-1] = c # b 번째 수를 c로 변경 !
    else: # a == 2 -> 구간 합 구하기
        total = 0
        for i in range(b-1, c):
            total += data[i]
        print(total)