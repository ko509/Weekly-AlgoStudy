import sys
import heapq
input = sys.stdin.readline

N = int(input())

queue = [] # 최소 힙
for i in range(N):
    data = list(map(int, input().split()))
    for x in data:
        if len(queue) < N:
            heapq.heappush(queue, x)
        else:
            if queue[0] < x:
                heapq.heappop(queue) # 가장 작은 수
                heapq.heappush(queue, x)
print(queue[0])

