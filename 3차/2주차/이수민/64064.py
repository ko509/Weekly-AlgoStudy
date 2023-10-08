from math import factorial
from collections import Counter
from collections import defaultdict


def cal(n,r):

    return factorial(n)//(factorial(n-r)*factorial(r))
    
    
    
    
def find(user_id,ban):
    global use_cnt
    cnt = 0
    for u in user_id:
        if len(u) != len(ban):
            continue
        
        u_tmp = list(u)
        ban_tmp = list(ban)
        
        fleg = 0 
        for i in range(len(u)):
            if ban_tmp[i] == '*':
                continue
            else:
                if ban_tmp[i] != u_tmp[i] : #한번이라도 다르면 볼필요없음
                    fleg = 1
                    break
        
        if fleg == 0 :
            use_cnt[u] += 1
            cnt+=1
        
                    
            
    return cnt


def solution(user_id, banned_id):
    global use_cnt
    
    answer = 1
    banned_id = Counter(banned_id)
    use_cnt = defaultdict(int)
    print(banned_id)
    
    for ban in banned_id :
        print(ban)
        answer *= cal(find(user_id,ban),banned_id[ban])
        
    jung = 1
    k = 0
    for i in use_cnt:
        
        if use_cnt[i]>1:
            k=0    
            for j in range(2,use_cnt[i]+1):
                k += cal(use_cnt[i],j)
                print(k)
    
        jung *= k
            
        
    
    
    return answer-jung

############################################################## 위는 수학적으로 풀어보려고 한것 아래는 하나하나 일치하는 것 세어본것
from itertools import permutations

def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False

        for j in range(len(users[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != users[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    user_permutation = list(permutations(user_id, len(banned_id)))
    ban_set = []

    for users in user_permutation:
        if not check(users, banned_id):
            continue
        else:
            users = set(users)
            if users not in ban_set:
                ban_set.append(users)

    return len(ban_set)




print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]))
print("??")
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))