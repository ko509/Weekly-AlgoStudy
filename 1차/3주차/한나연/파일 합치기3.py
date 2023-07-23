import sys
import heapq

for _ in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(arr)   # 최소힙
    result = 0

    while len(arr) >= 2:
        f = heapq.heappop(arr)
        s = heapq.heappop(arr)
        result += (f + s)
        heapq.heappush(arr, (f + s))
    print(result)