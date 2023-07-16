# https://www.acmicpc.net/problem/14499

n, m, x, y, k = map(int, input().split())
# 지도에 쓰여 있는 수
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
# 명령
command = list(map(int, input().split()))


