import heapq
# heapq 는 원래 최소힙 제공함

T = int(input())
for _ in range(T):
    n = int(input())
    queue = list(map(int, input().split()))
    total = 0

    heapq.heapify(queue)
    # queue = []
    # for i in data:
    #     heapq.heappush(queue, i)
    while len(queue) > 1:
        x = heapq.heappop(queue)
        y = heapq.heappop(queue)

        total += (x+y)
        heapq.heappush(queue, x+y)

    print(total)
