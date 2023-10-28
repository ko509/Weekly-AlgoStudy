from collections import deque
 
m,n = map(int, input().split())
map = [ list(map(int,input().rstrip())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
 
def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = 0
    while q:
        x,y = q.popleft()
        if x==n-1 and y==m-1: #도착
            return visited[x][y]
 
        for i in range(4): 
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==-1:
                
                if map[nx][ny] == 0: #방
                    
                    visited[nx][ny] = visited[x][y]
                    q.appendleft((nx,ny))
                else: #벽
                    visited[nx][ny] = visited[x][y]+1
                    q.append((nx, ny))
print(bfs())