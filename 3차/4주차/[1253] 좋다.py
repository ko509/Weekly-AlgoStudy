# https://www.acmicpc.net/problem/1253
answer = 0
N = int(input())
data = list(map(int, input().split()))
data.sort()

# 이분 탐색
for i in range(N):
    now = data[i] # 검증하는 숫자
    left = 0
    right = N - 1
    while left < right:
        good = (data[left] + data[right])
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue
        if good == now:
            answer += 1
            break
        elif good < now: # 작은 경우
            left += 1
        else:
            right -= 1

print(answer)