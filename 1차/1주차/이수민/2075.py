from queue import PriorityQueue


n = int(input())
queue = PriorityQueue(maxsize=n)
for _ in range(n):
    tmp = list(map(int, input().split()))
    print(tmp)
    for i in tmp:
        if not queue.full():
            queue.put(i)
            continue
        
        if queue.full() and queue.queue[0] < i:
            queue.get()
            queue.put(i)
            

print(queue.get())