import sys
sys.setrecursionlimit(111111)

def find(start,n):
    global tmp 
    global total
    
    if visited[n] == 1:
        if n == start:
            tmp = True
        else:
            tmp = False
        return
    Circle.append(n)
    visited[n] = 1
    
    find(start,S[n]-1)


T = int(input())
for _ in range(T):
    n = int(input())
    S = list(map(int,input().split()))
    
    tmp = 0
    total = 0
    visited = [0 for _ in range(n)]
    for i in range(n):
        if i == S[i]-1:
            visited[i] = 1
            total +=1
            continue 
        if visited[i] == 1:
            continue
        
        Circle = []
        find(i,i)
        if tmp :
            total += len(Circle)
            
    print(n-total)
    
        