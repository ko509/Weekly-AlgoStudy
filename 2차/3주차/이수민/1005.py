from collections import defaultdict
from collections import deque
 

T = int ( input ())
for _ in range ( T ):
    N , K = map ( int , input (). split ())
    S = list ( map ( int , input (). split ()))
 
    out = [[] for _ in range(N+1)]
    SS = [0] * (N + 1)   
    
    
    for _ in range ( K ):
        X , Y = map ( int , input (). split ())
        out[Y].append(X)

    target = int(input())

    start = deque()
    
    start.append(target)
    
    end = []
    

    SS[target] = S[target-1]
    while start:
        a = start.popleft()
        
        if not out[a]:
            end.append(a)
            continue
        
        for i in out[a]:
            if SS[i] < SS[a] + S[i-1]:
                SS[i] = SS[a] + S[i-1]
                start.append(i)
    maxV = 0
    for i in end:                       # 도착점들 중에 가장 큰 값을 뽑아내기
        if SS[i] > maxV:
            maxV = SS[i]
    print(maxV)
  