from collections import deque

def find(target,k):
    cnt = 0
    que = deque()
    visited = [0 for _ in range(N)]
    que.append(target)
    visited[target] = 1
    while que:
        v = que.popleft()
        for i in range(N):
            if not visited[i] and S[v][i] != 0:
                #print((i,S[v][i]))
                if S[v][i] >= k: #S[v][i]가 k보다 작을 경우는 더이상 볼필요가 없음 -> 작다면 어차피 이 번호를 거쳐서 가는 경로는 모두 k보다 작을것이므로. 
                    cnt +=1
                    visited[i] = 1
                    que.append(i)
                    
    return cnt           
            
    

N, Q = map(int, input().split())
S = [[0 for _ in range(N)]for _ in range(N)]

for _ in range(N-1):
    a,b,c = map(int, input().split())
    S[a-1][b-1] = c
    S[b-1][a-1] = c
    

for _ in range(Q):
    a,b = map(int, input().split()) #k가 a일 때, b번 동영상
    print(find(b-1,a))

    
    
#위와 같은 식으로 할경우(경로 없는 것을 0으로 채운것) 시간초과 걸림
#경로 있는 것만 돌 수 있도록 해야 시간초과 안걸림 