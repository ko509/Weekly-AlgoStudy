N = int(input())
D = []
answer = []
log = []
for _ in range(N):
    s = input()
    
    if len(s) == 1:
        ch = s
    else :
        ch, num = s.split()
        num = int(num)
    
    if ch == 'a':
        D.append(num)
    elif ch == 's':
        D.pop()
    else :
        if num == 1:
            D = []
        else :
            D = log[num-2].copy()
        
    
    
    if len(D) == 0:
        print(-1)
        
    else:
        print(D[-1])
        

    log.append(D.copy())
    
