def find(total, index,x,y):
    global total_M
    if x == N-1:
        total_M = min(total_M, total)
        return
    
    for i in range(3):

        new_x = x + dx[i]
        new_y = y + dy[i]

        #같은 방향 한번 더 안가게 하기
        if index == i:
            continue
        
        #밖으로 안벗어나게하기
        if not(0<=new_x<N and 0<=new_y<M):
            continue
        find(total+S[new_x][new_y],i,new_x,new_y)


dx = [1,1,1]
dy = [-1,0,1]
N,M = map(int, input().split())
total_M = float("inf")
S= []
for _ in range(N):
    S.append(list(map(int, input().split())))


for i in range(M):
    find(S[0][i],-1,0,i)

print(total_M)
