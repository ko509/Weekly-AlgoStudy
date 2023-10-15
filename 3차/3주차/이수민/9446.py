import sys
sys.setrecursionlimit(111111)

def find(n):
    global total
    global Circle
    
    Circle.append(n)
    visited[n] = 1
    next = S[n]-1
    
    if visited[next] == 1:
        if next in Circle:
            Circle = Circle[Circle.index(next):]
        else :
            Circle = []
        return
    
    
    
    find(S[n]-1)


T = int(input())
for _ in range(T):
    n = int(input())
    S = list(map(int,input().split()))
    
    total = 0
    visited = [0 for _ in range(n)]
    for i in range(n):
        if visited[i] == 1:
            continue
        
        Circle = []
        find(i)
        total += len(Circle)
            
            
             
    print(n-total)