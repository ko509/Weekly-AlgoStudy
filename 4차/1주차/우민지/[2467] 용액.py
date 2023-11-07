# https://www.acmicpc.net/problem/2467
N = int(input())
data = list(map(int, input().split()))

left, right = 0, N-1
near_zero = abs(data[left] + data[right])
answer = [left, right]
while left < right:
    mix = data[left] + data[right]
    if abs(near_zero) >= abs(mix):
        near_zero = abs(mix)
        answer = [data[left], data[right]]
    if mix == 0:
        near_zero = 0
        answer = [data[left], data[right]]
        break
    elif mix > 0:
        right -= 1
    else: # mix < 0
        left += 1

print(*answer)