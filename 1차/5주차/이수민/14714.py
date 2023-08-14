from collections import deque

def bfs():
    
    S = deque([(A,'A',0),(B,'B',0)])
    visted = [0 for _ in range(N+1)]
    visted[A] = ('A',0)
    visted[B] = ('B',0)
    while S:
        
        index, AB, depth = S.popleft()
        if depth == 3:
            return
        # if visted[index] != 0:
        #     vi, i = visted[index]
        #     if vi != AB and depth-1 == i:
        #         return i+depth
        
        if AB == 'A':
            D = DA
        else :
            D = DB
        
        if index + D > N:
            tmp = (index + D) % N
        else:
            tmp = index + D
            
        S.append((tmp ,AB,depth+1))
        
        if visted[tmp] != 0:
            vi, i = visted[tmp]
            if vi != AB and AB == 'B' and depth-1 == i:
                print(i+depth+1)
                return
            
            elif vi != AB and AB == 'A' and depth == i:
                print(i+depth+1)
                return
            
        visted[tmp] = (AB,depth+1)
        ###################################
        if index - D <= 0 :
            tmp = abs(index-D)
            tmp = N- tmp
        else :
            tmp = index - D
            
        S.append((tmp,AB,depth+1))
        
        
        if visted[tmp] != 0:
            vi, i = visted[tmp]
            if vi != AB and AB == 'B' and depth-1 == i:
                print(i+depth+1)
                return
            
            elif vi != AB and AB == 'A' and depth == i:
                print(i+depth+1)
                return
        visted[tmp] = (AB,depth+1)
            
                

N,A,B,DA,DB = map(int,input().split())
if N % 2 == 0 and DA == N//2 and DB == N//2 and (A+N//2!=B and B+N//2!=A):
    print("Evil Galazy")
else :
    bfs()
    
