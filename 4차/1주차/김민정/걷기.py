from sys import stdin
input = stdin.readline

x, y, w, s = map(int, input().split())
res = 0

if 2*w < s:
    res = (x + y) * w
else:
    step = min(x, y)
    res = step * s
    remain = abs(x - y)

    if w > s:
        if remain % 2 == 0:
            res += remain * s
        else:
            res += (remain - 1) * s + w
    else:
        res += remain * w

print(res)
