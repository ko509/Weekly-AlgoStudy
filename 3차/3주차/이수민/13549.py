from collections import deque

def find():
    
    visited = [-1 for _ in range(end+1)]
    visited[N] = 0
    que = deque()
    que.append(N)

    while que:
        a = que.popleft()
        
        if a == K :
            return visited[a]
 
        if 0<=a*2 <end+1 and visited[a*2] == -1 :
            visited[a*2] = visited[a]
            que.appendleft(a*2)
            
        if 0<=a-1 <end+1 and visited[a-1] == -1 :
            visited[a-1] = visited[a]+1
            que.append(a-1)
            
        if 0<=a+1 <end+1 and visited[a+1] == -1 :
            visited[a+1] = visited[a]+1
            que.append(a+1)
            
    
        
                


N, K = map(int, input().split())
end = 100000
print(find())


#마지막에 99%에서 틀려서 질문게시판 반례를 보니 4 6 이 1이 나와야 했다
#그래서 혹시나 해서 두번째와 세번째 if를 바꿨더니 됐다.. 
#근본적인 해결이 아닐텐데.. 
#반례와 상관없이 a-1이 먼저 와야하는 이유가 뭐지...?ㅠ