# https://www.acmicpc.net/problem/3020
n, h = map(int, input().split())

down = [0] * (h+1) # 짝수
up = [0] * (h+1)  # 홀수

# 누적합을 위해 카운트
for i in range(n):
    if i % 2 == 0:
        down[int(input())] += 1
    else:
        up[int(input())] += 1

for i in range(h-1, 0, -1):
    down[i] += down[i+1]
    up[i] += up[i+1]

min_value = n # 장애물 최솟값
count = 0 # 최솟값의 개수

# 갱신 & 저장 로직
for i in range(1, h+1):
    tmp = (down[i] + up[h - i +1])
    if min_value > tmp:
        min_value = tmp
        count = 1
    elif min_value == tmp:
        count += 1
print(min_value, count)