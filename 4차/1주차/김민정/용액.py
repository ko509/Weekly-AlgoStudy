from sys import stdin
input = stdin.readline

N = int(input())
liquid = list(map(int, input().split()))

l, r = 0, N - 1
l1, l2 = liquid[l], liquid[r]
min_density = abs(liquid[l] + liquid[r])

while l < r:
    density = liquid[l] + liquid[r]

    if abs(density) < min_density:
        l1, l2 = liquid[l], liquid[r]
        min_density = abs(density)

        if density == 0:
            break

    if density < 0:
        l += 1
    else:
        r -= 1

print(l1, l2)
