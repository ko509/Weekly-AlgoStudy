#투포인터를 모르던 나에게 개념을 알게 해준 문제
#근데.... 시간때문에 소수구하는게 더 어려웠다^^

import math

def GetPrimeEratosthenes(n):
    chk = [True]*(n+1)
    res = []
    chk[0], chk[1] = False, False
    for i in range(2, int(math.sqrt(n))+1):
        if chk[i]:
            res.append(i)
            j = 2
            while i*j <= n:
                chk[i*j] = False
                j += 1
    res = [x for x in range(n+1) if chk[x]]
    return res
        
n = int(input())
S = []
S = GetPrimeEratosthenes(n)

end = 0
total = 0
cnt = 0
for start in range(len(S)):
    while total < n and end < len(S):
        total += S[end]
        end += 1
    
    if n == total :
        cnt += 1
    
    total -= S[start]
        
        
print(cnt)    
        