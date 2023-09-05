def A(i):
    dic = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    if i>= 10:
        return dic[i]
    else:
        return str(i)

def trans(n,num):
    S = []
    
    if num == 0:
        return ["0"]
    
    while num > 0 :
        r = num % n  # 나머지
        
        
        if num == 0:
            S.append(A(num))
            break
        S.append(A(r))
        
        num = num // n #몫
        
        
    
    return S[::-1]
            
        

def solution(n, t, m, p):
    answer = []
    S = []
    SS = ""
    
    for i in range(0,t**2):
        S += list(trans(n,i))
    
    for i in range(0,t):
        answer.append(S[i*m+(p-1)])
        
    return "".join(answer)