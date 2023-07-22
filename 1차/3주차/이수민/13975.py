#from queue import PriorityQueue 를 썼는데, 시간초과가 걸렸다... 
#그리고 Greedy 할때마다 느끼는거지만...
#해당 알고리즘은 그냥 잘 생각안나면 넘기는게 답이지 않을까 하는...
#대부분 어떤 알고리즘을 써서 풀리는 게 아니라 그냥 어떻게 하면 최소일지 알아서 생각하는게 문제...
import sys
import heapq

T = int(input())
for _ in range(T):
    N = int(input())
    total = 0
    
    queue = []
    
    for l in map(int, sys.stdin.readline().split()):
        heapq.heappush(queue,l)
        
    while len(queue) > 1:
        a = heapq.heappop(queue)
        b = heapq.heappop(queue)
        total += a + b
        heapq.heappush(queue,a + b)
        
    print(total)
