from sys import stdin
input = stdin.readline

N = int(input())
liquid = sorted(list(map(int, input().split())))

left = 0
right = N - 1

t_left = left
t_right = right
ans = liquid[left] + liquid[right]

while left < right:
    tmp = liquid[left] + liquid[right]

    if abs(tmp) < abs(ans):
        ans = tmp
        t_left = left
        t_right = right

        if ans == 0:
            break

    if tmp < 0:
        left += 1
    else:
        right -= 1

print(liquid[t_left], liquid[t_right])
