#다익스트라
#heap을 사용하고, 가중치의 비교를 사용하기 때문에 가중치가 앞에 가는게 중요

import heapq

def find(x,y,total):
    heap = []
    heapq.heappush(heap, (total,x,y))
    visited[0][0] = 1
    while heap:
        
        total, x,y = heapq.heappop(heap)    
        if x == N-1 and y == N-1 :
            
            print(total)
            return
    
        for i in range(4):
            new_x, new_y = x+dx[i], y+dy[i]
            
            if not(0<=new_x<N and 0<=new_y<N):
                continue
            
            if visited[new_x][new_y] == 1:
                continue
            
            visited[new_x][new_y] = 1
            
            if S[new_x][new_y] == 0  : #검정색
                heapq.heappush(heap,(total+1,new_x,new_y))
            else : #흰색
                heapq.heappush(heap,(total,new_x,new_y))
                
        

            


N = int(input())
S = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(N):
    S.append(list(map(int, list(input()))))


find(0,0,0)
