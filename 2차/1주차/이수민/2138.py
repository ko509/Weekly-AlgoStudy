def trans(cur):
    return '1' if cur=='0' else '0'



def find2(B,F):
    A = B[:]
    tmp =  0
    
    for i in range(1,n):
        if A[i-1] == F[i-1]:
            continue
        
        tmp += 1
        #앞의 스위치는 해당자리를 벗어나면 바로 다음 스위치에서만 키거나 끌 수 있기 때문에 앞전구가 답이랑 다르다면 무조건 킨다
        if i == n-1 :
            A[n-1] = trans(A[n-1])
            A[n-2] = trans(A[n-2])
        else:
            A[i] = trans(A[i])
            A[i+1] = trans(A[i+1])
            A[i-1] = trans(A[i-1])
            
    return tmp if A == F else 1e9


n = int(input())
B = list(input())
F = list(input())

visited = [0 for _ in range(n)]
a = find2(B,F)
B[0] = trans(B[0])
B[1] = trans(B[1])
a = min(a,find2(B,F)+1)
print(a if a!= 1e9 else -1)
        