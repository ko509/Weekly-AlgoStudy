from sys import stdin
from collections import deque
input = stdin.readline

N, K = map(int, input().split())
MAX_LEN = 100001

visited = [0] * MAX_LEN
time = [0] * MAX_LEN

queue = deque()
queue.append(N)
visited[N] = 1

while queue:
    cur_pos = queue.popleft()

    if cur_pos * 2 < MAX_LEN and not visited[cur_pos * 2]:
        queue.appendleft(cur_pos * 2)
        visited[cur_pos * 2] = 1
        time[cur_pos * 2] = time[cur_pos]

    if cur_pos - 1 >= 0 and not visited[cur_pos - 1]:
        queue.append(cur_pos - 1)
        visited[cur_pos - 1] = 1
        time[cur_pos - 1] = time[cur_pos] + 1
        
    if cur_pos + 1 < MAX_LEN and not visited[cur_pos + 1]:
        queue.append(cur_pos + 1)
        visited[cur_pos + 1] = 1
        time[cur_pos + 1] = time[cur_pos] + 1

print(time[K])
