import copy

def count_right(S,x,y):
    global visited
    cnt = 0
    for b in range(y+1,M):
        if S[x][b] == 6:
            return cnt
        if S[x][b] in [1,2,3,4,5]:
            continue
        if visited[x][b] == 1:
            continue
        
        visited[x][b] = 1
        cnt+=1
    return cnt
def count_left(S,x,y):
    cnt = 0
    global visited
    for b in range(y-1,-1,-1):
        if S[x][b] == 6:
            return cnt
        if S[x][b] in [1,2,3,4,5]:
            continue
        if visited[x][b] == 1:
            continue
        
        visited[x][b] = 1
        cnt+=1
    return cnt
def count_up(S,x,y):
    cnt = 0
    global visited
    for a in range(x-1,-1,-1):
        if S[a][y] == 6:
            return cnt
        if S[a][y] in [1,2,3,4,5]:
            continue
        if visited[a][y] == 1:
            continue
        
        visited[a][y] = 1
        cnt+=1
    return cnt
def count_down(S,x,y):
    cnt = 0
    global visited
    for a in range(x+1,N):
        
        if S[a][y] == 6:
            return cnt
        if S[a][y] in [1,2,3,4,5]:
            continue
        if visited[a][y] == 1:
            continue
        
        visited[a][y] = 1
        cnt+=1
    return cnt

    

def A(index,x,y):
    global visited
    indexes = list(map(int,index.split()))
    cnt = 0
    for i in indexes:
        if i == 0 :
            cnt += count_up(S,x,y)
        elif i == 1:
            cnt += count_right(S,x,y)
        elif i== 2:
            cnt += count_down(S,x,y)
        elif i == 3 :
            cnt += count_left(S,x,y)
        
       
    return cnt
    
def find(index,cnt):
    global total
    global visited
    if index == len(cctv_index):
        total = min(total, CNT - cnt)
        return
    
    
    new_x,new_y = cctv_index[index]
    
    k = S[new_x][new_y] -1
    tmp_visited = copy.deepcopy(visited)
    
    
    for i in range(len(cctv[k])):
        find(index+1,cnt+A(cctv[k][i],new_x,new_y))
        visited = copy.deepcopy(tmp_visited)
            
            
        
        

N, M = map(int, input().split())
S = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cctv_index = []
cctv = [['0','1','2','3'],['3 1','0 2'],['0 1','1 2','2 3','3 0'],['0 1 2','1 2 3','2 3 0','3 0 1'],['0 1 2 3']]
visited = [[0 for _ in range(M)] for _ in range(N)]
tmp_x = 0
total = N*M
cctv_5 = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    S.append(tmp)
    for i in range(M):
        if tmp[i] in [1,2,3,4]:
            total -= 1
            cctv_index.append((tmp_x,i))
        elif tmp[i] == 5:
            total -=1
            cctv_5.append((tmp_x,i))     
        elif tmp[i] == 6:
            total -=1
            
    
    tmp_x += 1



for i in cctv_5:
    a,b = i
    total -=A(cctv[4][0],a,b)

CNT = total
find(0,0)
print(total) 
    
            
    
    
    
