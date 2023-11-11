# https://www.acmicpc.net/problem/1459
X, Y, W, S = map(int, input().split())

# 1. 평행 이동
a = (X+Y) * W
# 2. 대각선 이동 > 대각선만
if (X+Y)%2 == 0:
    b = max(X, Y) * S
else: # 3. 대각선 이동 > 홀수이므로 대각선 + 평행 1칸
    b = (max(X, Y)-1) * S + W

# 4. 평행 이동 + 대각선 이동
c = min(X, Y) * S + abs(X-Y) * W

print(min(a, b, c))